// content.js

// Load Readability library from local path
const script = document.createElement('script');
script.src = chrome.runtime.getURL('libs/Readability.min.js');
script.onload = () => {
  console.log('Readability library loaded.');
};
script.onerror = () => {
  console.error('Failed to load Readability library.');
};
document.head.appendChild(script);
