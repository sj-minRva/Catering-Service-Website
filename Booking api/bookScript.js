// bookScript.js
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
        document.getElementById('response').innerText = data.message;
        if (data.message === "Booking successful!"){
            document.getElementById("saveButton").addEventListener("click", function(event) {
                event.preventDefault();
                document.getElementById('response').innerText = "Saved successfully!";
                document.getElementById("submitButton").disabled = false;
            });

            document.getElementById("submitButton").addEventListener("click", function() {
                if (!this.disabled) {
                    window.location.href = "menuselect.html";
                }
            });
        }
        console.log('Success:', data);
    })
    .catch((error) => {
        document.getElementById('response').innerText = `Error: ${error.message}`;
        console.error('Error:', error);
    });
});