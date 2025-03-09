document.getElementById('customerForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;

    const data = {
        name: name,
        email: email,
        phone: phone
    };

    fetch('http://127.0.0.1:5000/api/customers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = 'Data submitted successfully!';
        console.log('Success:', data);
    })
    .catch((error) => {
        document.getElementById('response').innerText = 'Error submitting data.';
        console.error('Error:', error);
    });
});
