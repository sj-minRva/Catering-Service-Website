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
    fetch("http://127.0.0.1:5000/api/book", { // Updated port to 5000
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(bookingData)
    })
    .then(response => response.json())
    .then(data => {
        // Handle success response
        document.getElementById('response').innerText = "Booking successful! Redirecting...";
        console.log('Success:', data);

        // Redirect to menu selection after 2 seconds
        setTimeout(() => {
            window.location.href = "menuselect.html";
        }, 2000);
    })
    .catch((error) => {
        // Handle error response
        document.getElementById('response').innerText = `Error: ${error.message}`;
        console.error('Error:', error);
    });
});
