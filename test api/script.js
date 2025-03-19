document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("customerForm").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission

        // Get input values
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        // Check if fields are filled
        if (!name || !email || !password) {
            document.getElementById("response").innerText = "Please fill in all fields.";
            return;
        }

        const data = { name, email, password };

        // Send data to Flask API
        fetch("http://127.0.0.1:5000/api/customers", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("response").innerText = "Error: " + data.error;
            } else {
                document.getElementById("response").innerText = "Data submitted successfully!";
                setTimeout(() => {
                    window.location.href = "menu.html"; // Redirect to menu.html after success
                }, 1500);
            }
        })
        .catch(error => {
            console.error("Error:", error);
            document.getElementById("response").innerText = "Failed to connect to the server.";
        });
    });

    // Toggle Password Visibility
    document.getElementById("togglePassword").addEventListener("click", function () {
        const passwordField = document.getElementById("password");
        passwordField.type = passwordField.type === "password" ? "text" : "password";
        this.textContent = passwordField.type === "password" ? "Show" : "Hide";
    });
});
