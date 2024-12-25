const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
  document.getElementById("password").addEventListener("input", function () {
    const password = this.value;
    const strengthMessage = document.getElementById("password-error");

    let strength = 0;

    if (password.length >= 8) strength++;
    if (password.match(/[A-Z]/)) strength++;
    if (password.match(/[a-z]/)) strength++;
    if (password.match(/[0-9]/)) strength++;
    if (password.match(/[@$!%*?&]/)) strength++;

    switch (strength) {
        case 0:
        case 1:
            strengthMessage.textContent = "Weak";
            strengthMessage.style.color = "red";
            break;
        case 2:
        case 3:
            strengthMessage.textContent = "Medium";
            strengthMessage.style.color = "orange";
            break;
        case 4:
        case 5:
            strengthMessage.textContent = "Strong";
            strengthMessage.style.color = "green";
            break;
    }
});

});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});
