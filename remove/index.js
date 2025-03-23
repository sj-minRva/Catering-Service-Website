const express = require('express');
const mysql = require('mysql2');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// MySQL Connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'your_password',
    database: 'event_management'
});

db.connect(err => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
    } else {
        console.log('Connected to MySQL');
    }
});

// Endpoint to Get Customer Data
app.get('/api/customers', (req, res) => {
    db.query('SELECT * FROM customers', (err, results) => {
        if (err) {
            res.status(500).send('Error fetching customers');
        } else {
            res.json(results);
        }
    });
});

// Endpoint to Send Email
app.post('/send-email', (req, res) => {
    const { email, name } = req.body;

    // Nodemailer Setup
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'your_email@gmail.com',
            pass: 'your_email_password'
        }
    });

    const mailOptions = {
        from: 'your_email@gmail.com',
        to: email,
        subject: 'Event Confirmation',
        text: `Hi ${name},\n\nYour event has been successfully confirmed. Thank you for choosing us!\n\nBest regards,\nEvent Management Team`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error('Error sending email:', error);
            res.status(500).send('Failed to send email');
        } else {
            console.log('Email sent:', info.response);
            res.status(200).send('Email sent successfully');
        }
    });
});

// Start Server
app.listen(5000, () => {
    console.log('Server running on port 5000');
});
