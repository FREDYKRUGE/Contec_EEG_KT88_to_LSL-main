// Variables to manage the reload state and interval
let isReloading = true;
let reloadInterval;

// Function to start reloading the page
function startReloading() {
    if (!reloadInterval) {
        reloadInterval = setInterval(() => {
            location.reload();
        }, 3000); // Reload every 3 seconds
    }
}

// Function to stop reloading the page
function stopReloading() {
    if (reloadInterval) {
        clearInterval(reloadInterval);
        reloadInterval = null;
    }
}

// Toggle function for the button
function toggleReloading() {
    const reloadButton = document.getElementById("reloadButton");
    const reloadStatus = document.getElementById("reloadStatus");

    if (isReloading) {
        stopReloading();
        reloadButton.textContent = "Start Reloading";
        reloadStatus.textContent = "Page is not reloading!";
        reloadButton.classList.remove("btn-danger");
        reloadButton.classList.add("btn-success");
    } else {
        reloadButton.textContent = "Stop Reloading";
        reloadStatus.textContent = "Page is reloading...";
        reloadButton.classList.remove("btn-success");
        reloadButton.classList.add("btn-danger");

        // Reload immediately
        location.reload();
    }
    isReloading = !isReloading;
}

// Set up initial state
document.addEventListener("DOMContentLoaded", () => {
    const reloadButton = document.getElementById("reloadButton");
    const reloadStatus = document.getElementById("reloadStatus");

    // Default state: Reloading
    startReloading();
    reloadButton.textContent = "Stop Reloading";
    reloadStatus.textContent = "Page is reloading...";
    reloadButton.classList.add("btn-danger");

    // Attach click event listener to the button
    reloadButton.addEventListener("click", toggleReloading);
});
