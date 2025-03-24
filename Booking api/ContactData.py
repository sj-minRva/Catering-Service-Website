from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend interaction

# Function to establish database connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "Catering"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root")
    )

# API to save contact form submissions
@app.route('/api/enquiries', methods=['POST'])
def save_enquiry():
    try:
        data = request.json
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        if not name or not email or not message:
            return jsonify({"error": "All fields are required"}), 400

        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO enquiries (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, message))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": "Enquiry submitted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to fetch contact form submissions
@app.route('/api/enquiries', methods=['GET'])
def fetch_enquiries():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Fetch latest entries first
        query = "SELECT name, email, message FROM enquiries ORDER BY submitted_at DESC"
        cursor.execute(query)
        enquiries = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(enquiries), 200
    except Exception as e:
        print("Error fetching enquiries:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5005)  # Running on port 5005
