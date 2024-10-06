// popup.js

document.addEventListener('DOMContentLoaded', () => {
    const summaryDiv = document.getElementById('summary');
    const refreshButton = document.getElementById('refresh');
  
    async function getSummary() {
      summaryDiv.innerHTML = '<p>Loading summary...</p>';
  
      try {
        // Get the active tab
        const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        if (!tab) {
          throw new Error('No active tab found.');
        }
  
        // Execute the content script to get the page content
        const [result] = await chrome.scripting.executeScript({
          target: { tabId: tab.id },
          func: extractContent,
        });
  
        const pageContent = result.result;
        console.log('Extracted Content:', pageContent);
  
        if (!pageContent || pageContent.trim().length === 0) {
          throw new Error('No content extracted from the page.');
        }
  
        // Summarize the content
        const summary = summarize(pageContent, 5); // Summarize to 5 sentences
        summaryDiv.innerHTML = `<p>${summary}</p>`;
      } catch (error) {
        console.error('Error generating summary:', error);
        summaryDiv.innerHTML = `<p>Error generating summary: ${error.message}</p>`;
      }
    }
  
    refreshButton.addEventListener('click', getSummary);
  
    // Initial summary generation
    getSummary();
  });
  
  // Function to extract content using Readability
  function extractContent() {
    try {
      // Check if Readability is loaded
      if (typeof Readability === 'undefined') {
        console.error('Readability library is not loaded.');
        return document.body.innerText;
      }
  
      const doc = new DOMParser().parseFromString(document.documentElement.outerHTML, 'text/html');
      const reader = new Readability(doc);
      const article = reader.parse();
  
      return article && article.textContent ? article.textContent : document.body.innerText;
    } catch (error) {
      console.error('Error in extractContent:', error);
      return document.body.innerText;
    }
  }
  