document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const urlInput = document.getElementById("url");
  const submitButton = document.querySelector(".btn-primary");
  const languageSelect = document.getElementById("language");

  // Create a loading spinner and progress bar
  const loadingContainer = document.createElement("div");
  loadingContainer.classList.add("loading-container");
  loadingContainer.innerHTML = `
      <div class="loading-spinner">
        <div class="spinner"></div>
        <p>Processing...</p>
        <div class="progress-bar-container">
          <div class="progress-bar"></div>
        </div>
      </div>
    `;
  loadingContainer.style.display = "none";
  document.body.appendChild(loadingContainer);

  // Function to update progress bar
  function updateProgressBar(progress) {
    const progressBar = document.querySelector(".progress-bar");
    if (progressBar) {
      progressBar.style.width = `${progress}%`;
    }
  }

  // Simulate progress bar fill using setInterval
  function simulateProgress() {
    let progress = 0;
    const interval = setInterval(function () {
      if (progress >= 100) {
        clearInterval(interval); // Stop progress after reaching 100%
        form.submit(); // Submit the form after progress is 100%
      } else {
        progress += 1;
        updateProgressBar(progress);
      }
    }, 20); // Update every 20 milliseconds to smoothly reach 100%
  }

  // Validate URL Input
  urlInput.addEventListener("input", function () {
    if (
      !urlInput.value.startsWith("http://") &&
      !urlInput.value.startsWith("https://")
    ) {
      urlInput.style.border = "2px solid red";
    } else {
      urlInput.style.border = "2px solid green";
    }
  });

  // Handle form submission
  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent immediate form submission

    // Show loading container and start progress
    loadingContainer.style.display = "flex";
    updateProgressBar(0); // Reset progress bar before starting
    simulateProgress(); // Start simulating progress
  });
});
