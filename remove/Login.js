document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("customerForm");
    const submitButton = document.getElementById("submitBtn");

    
        // Get input values
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        // Validate input fields
        if (!name || !email || !password) {
            errorDiv.textContent = "All fields are required.";
            return; // Stop if inputs are empty
        }

        // Check if details match the given credentials
        if (name === "Admin" && email === "rheamaria13@gmail.com" && password === "1234") {
            errorDiv.textContent = "Successful"; // Clear error message
            window.location.href = "adminLogin.html"; // Redirect to admin page
        } else {
            errorDiv.textContent = "Incorrect login details.";
        }
    

    // Toggle Password Visibility
    const togglePassword = document.getElementById("togglePassword");
    togglePassword.addEventListener("click", function () {
        const passwordField = document.getElementById("password");
        const type = passwordField.type === "password" ? "text" : "password";
        passwordField.type = type;

        // Toggle icon classes
        this.classList.toggle("fa-eye");
        this.classList.toggle("fa-eye-slash");
    });
});
