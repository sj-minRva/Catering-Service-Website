from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)

# Function to establish database connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'Catering'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'root')
    )

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the booking API!"

@app.route('/api/book', methods=['POST'])
def book_event():
    data = request.json
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Insert the booking into the database
        query = """
            INSERT INTO bookings (name, contact, email, place, city, event_type, guests, food_type, event_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data['name'], data['contact'], data['email'], data['place'],
            data['city'], data['eventType'], data['guests'], data['foodType'], data['date']
        ))
        connection.commit()

        # Get the newly created booking ID
        booking_id = cursor.lastrowid  # Fetch the auto-incremented ID of the newly inserted record

        return jsonify({
            "message": "Booking successful!",
            "bookingId": booking_id
        }), 201

    except mysql.connector.Error as err:
        print("Database Error:", err)
        return jsonify({"message": "Booking failed!", "error": str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
