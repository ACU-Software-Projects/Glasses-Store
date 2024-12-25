// Query selectors for buttons and container
const signInBtn = document.querySelector("#sign-in-btn");
const signUpBtn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

// Add event listener for the Sign-Up button
signUpBtn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");

    // Attach password strength validation listener when in sign-up mode
    const passwordInput = document.getElementById("password");
    passwordInput.addEventListener("input", () => {
        const password = passwordInput.value;
        const strengthMessage = document.getElementById("password-error");

        let strength = 0;

        // Check for various password strength criteria
        if (password.length >= 8) strength++;
        if (password.match(/[A-Z]/)) strength++;
        if (password.match(/[a-z]/)) strength++;
        if (password.match(/[0-9]/)) strength++;
        if (password.match(/[@$!%*?&]/)) strength++;

        // Display password strength feedback
        if (!strengthMessage) {
            // Create password strength message element if it doesn't exist
            const errorDiv = document.createElement("div");
            errorDiv.id = "password-error";
            passwordInput.parentElement.appendChild(errorDiv);
        }

        const strengthDisplay = document.getElementById("password-error");

        switch (strength) {
            case 0:
            case 1:
                strengthDisplay.textContent = "Weak";
                strengthDisplay.style.color = "red";
                break;
            case 2:
            case 3:
                strengthDisplay.textContent = "Medium";
                strengthDisplay.style.color = "orange";
                break;
            case 4:
            case 5:
                strengthDisplay.textContent = "Strong";
                strengthDisplay.style.color = "green";
                break;
        }
    });
});

// Add event listener for the Sign-In button
signInBtn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});

// Ensure password strength feedback disappears when leaving sign-up mode
signInBtn.addEventListener("click", () => {
    const strengthMessage = document.getElementById("password-error");
    if (strengthMessage) strengthMessage.remove();
});
