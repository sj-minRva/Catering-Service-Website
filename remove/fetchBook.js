function loadCustomers() {
    fetch('http://127.0.0.1:5000/api/customers') // Fetch data from the API
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById("customerTableBody");
            tableBody.innerHTML = ""; // Clear existing data

            data.forEach((customer) => {
                const row = `
                    <tr>
                        <td>${customer.id}</td>
                        <td>${customer.name}</td>
                        <td>${customer.contact}</td>
                        <td>${customer.email}</td>
                        <td>${customer.place}</td>
                        <td>${customer.city}</td>
                        <td>${customer.event_type}</td>
                        <td>${customer.guests}</td>
                        <td>${customer.food_type}</td>
                        <td>${customer.event_date}</td>
                        <td>
                            <button onclick="confirmCustomer(${customer.id})">Confirm</button>
                            <button onclick="notConfirmCustomer(${customer.id})">Reject</button>
                        </td>
                    </tr>
                `;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error("Error loading customers:", error));
}

window.onload = loadCustomers;

// Function for handling "Confirm" button clicks
function confirmCustomer(id) {
    console.log(`Customer with ID ${id} confirmed.`);
    // Add additional logic for confirming customer if needed
}

// Function for handling "Not Confirm" button clicks
function notConfirmCustomer(id) {
    console.log(`Customer with ID ${id} not confirmed.`);
    // Add additional logic for not confirming customer if needed
}
