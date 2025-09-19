<<<<<<< Updated upstream
from flask import Flask, jsonify
=======
from flask import Flask, jsonify, request
>>>>>>> Stashed changes
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

<<<<<<< Updated upstream
# Function to establish a database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Catering"
    )

# API Endpoint: Fetch and merge bookings and orders
@app.route('/merged-data', methods=['GET'])
def get_merged_data():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        query = """
                    SELECT 
            b.id AS booking_id,
            b.name,
            b.contact,
            b.event_date,
            b.guests,
            b.food_type,
            COALESCE(GROUP_CONCAT(o.item_name SEPARATOR ', '), 'No Orders') AS items,
            COALESCE(GROUP_CONCAT(o.quantity SEPARATOR ', '), 'No Orders') AS quantities
        FROM bookings b
        LEFT JOIN orders o ON b.id = o.bookingID
        GROUP BY b.id, b.name, b.contact, b.event_date, b.guests, b.food_type;

        """

        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        db.close()

        return jsonify(data)

    except mysql.connector.Error as err:
        return jsonify({"error": f"Database error: {str(err)}"}), 500

# Run the server on port 5007
if __name__ == '__main__':
    app.run(debug=True, port=5007)
=======
# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Update with your MySQL username
    password="",  # Update with your MySQL password
    database="your_database_name"  # Replace with your actual database name
)

# API Endpoint: Fetch merged table data
@app.route('/merged-data', methods=['GET'])
def get_merged_data():
    cursor = db.cursor(dictionary=True)
    query = """
        SELECT 
            b.id, b.name, b.contact, b.email, b.place, b.city, b.event_type, b.guests, b.food_type, b.event_date,
            GROUP_CONCAT(o.item_name SEPARATOR ', ') AS items,
            GROUP_CONCAT(o.quantity SEPARATOR ', ') AS quantity,
            GROUP_CONCAT(o.order_date SEPARATOR ', ') AS order_dates
        FROM bookings b
        LEFT JOIN orders o ON b.id = o.bookingID
        GROUP BY b.id;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

# API Endpoint: Add Booking
@app.route('/add-booking', methods=['POST'])
def add_booking():
    data = request.json
    cursor = db.cursor()
    query = """
        INSERT INTO bookings (name, contact, email, place, city, event_type, guests, food_type, event_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        data['name'], data['contact'], data['email'], data['place'],
        data['city'], data['event_type'], data['guests'], data['food_type'], data['event_date']
    ))
    db.commit()
    cursor.close()
    return jsonify({"message": "Booking added successfully"}), 201

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> Stashed changes
