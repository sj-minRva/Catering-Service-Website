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
        document.getElementById('response').innerText = data.message;
        console.log('Success:', data);
    })
    .catch((error) => {
        document.getElementById('response').innerText = `Error: ${error.message}`;
        console.error('Error:', error);
    });
});
