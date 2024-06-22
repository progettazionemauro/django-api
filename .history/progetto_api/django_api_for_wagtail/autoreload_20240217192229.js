// auto_reload.js

function autoRefreshPage() {
    window.location = window.location.href;
}

setInterval(autoRefreshPage, 10000); // Refresh the page every 10 seconds
