function removeMiniplayerButton() {
    const button = document.querySelector('button.ytp-miniplayer-button');
    if (button) {
      button.remove();
      console.log('Miniplayer button removed!');
    }
  }
  
  // Run when page loads
  window.addEventListener('DOMContentLoaded', removeMiniplayerButton);
  
  // Also run when navigating between videos (because YouTube is a SPA and doesn’t reload the full page)
  let observer = new MutationObserver(removeMiniplayerButton);
  observer.observe(document.body, { childList: true, subtree: true });
  