# bookapi.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)

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
    connection = None
    cursor = None
    try:
        data = request.json
        name = data['name']
        contact = data['contact']
        email = data['email']
        place = data['place']
        city = data['city']
        event_type = data['eventType']
        guests = data['guests']
        food_type = data['foodType']
        event_date = data['date']

        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO bookings (name, contact, email, place, city, event_type, guests, food_type, event_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, contact, email, place, city, event_type, guests, food_type, event_date))
        connection.commit()

        return jsonify({"message": "Booking successful!"}), 200
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return jsonify({"message": "Booking failed!", "error": str(err)}), 500
    except KeyError as err:
        print("Key Error:", err)
        return jsonify({"message": "Booking failed! Missing key in JSON data.", "error": str(err)}), 400
    except Exception as err:
        print("General Error:", err)
        return jsonify({"message": "Booking failed! An unexpected error occurred.", "error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(debug=True, port=5001)