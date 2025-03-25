document.getElementById("bookingForm").addEventListener("submit", function(event) {
    event.preventDefault();

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

    fetch("http://127.0.0.1:5001/api/book", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(bookingData)
    })
    .then(response => response.json())
    .then(data => {
        const responseElement = document.getElementById('response');

        if (data.message === "Booking successful!") {
            responseElement.innerText = `Saved successfully! Booking ID: ${data.bookingId}`;

            document.getElementById("saveButton").addEventListener("click", function(event) {
                event.preventDefault();
                responseElement.innerText = `Saved successfully! Booking ID: ${data.bookingId}`;
                document.getElementById("submitButton").disabled = false;

            });

            document.getElementById("submitButton").addEventListener("click", function() {
                window.location.href = "menuselect.html";
            });

        } else {
            responseElement.innerText = data.message;
        }
    })
    .catch((error) => {
        document.getElementById('response').innerText = `Error: ${error.message}`;
        console.error('Error:', error);
    });
});
