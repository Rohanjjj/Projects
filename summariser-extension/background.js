// content.js

// Listen for messages from the background script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    console.log('Message received:', request); // Debug log
    if (request.action === "toggleSidebar") {
      toggleSidebar();
    }
  });
  