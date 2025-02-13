document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("bookingForm").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form from submitting the default way

        // Fetching user inputs using getElementById
        const country = document.getElementById("country").value;
        const city = document.getElementById("city").value;
        const palace = document.getElementById("palace").value;
        const eventType = document.getElementById("eventType").value;
        const guests = document.getElementById("guests").value;
        const foodType = document.getElementById("foodType").value;
        const contact = document.getElementById("contact").value;
        const date = document.getElementById("date").value;
        const email = document.getElementById("email").value;

        // Store data in an object
        const formData = {
            country: country,
            city: city,
            palace: palace,
            eventType: eventType,
            guests: guests,
            foodType: foodType,
            contact: contact,
            date: date,
            email: email
        };

        console.log("Collected Form Data:", formData);

        // Send data to Flask API
        fetch("http://127.0.0.1:5000/api/book", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            console.log("Success:", data);
            alert("Booking submitted successfully!");
        })
        .catch(error => {
            console.error("Error:", error);
            alert("Failed to submit booking.");
        });
    });
});
