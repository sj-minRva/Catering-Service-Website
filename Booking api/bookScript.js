document.getElementById("bookingForm").addEventListener("submit", function(event) {
    event.preventDefault();

    // Collect form data
    const bookingData = {
        name: document.getElementById("Name").value.trim(),
        contact: document.getElementById("contact").value.trim(),
        email: document.getElementById("email").value.trim(),
        place: document.getElementById("place").value.trim(),
        city: document.getElementById("city").value.trim(),
        eventType: document.getElementById("eventType").value,
        guests: document.getElementById("guests").value,
        foodType: document.getElementById("foodType").value,
        date: document.getElementById("date").value
    };

    // Send data to Flask API
    fetch("http://127.0.0.1:5001/api/book", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(bookingData)
    })
    .then(response => response.json())
    .then(data => {
        
        document.getElementById("saveButton").addEventListener("click", function(event) {
            event.preventDefault(); // Prevents the default form submission for demonstration.
            document.getElementById('response').innerText = "Saved successfully!"; // Visual feedback.
            document.getElementById("submitButton").disabled = false; // Enable Submit button.
        });
        
        document.getElementById("submitButton").addEventListener("click", function() {
            if (!this.disabled) {
                window.location.href = "menu.html"; // Redirects to menu.html when enabled.
            }
        });
               
        
        console.log('Success:', data);
    })
    .catch((error) => {
        document.getElementById('response').innerText = `Error: ${error.message}`;
        console.error('Error:', error);
    });

    
});
