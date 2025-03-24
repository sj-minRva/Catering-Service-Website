from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend interaction

# Database connection function
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
        # Get JSON data from frontend
        data = request.json
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        if not name or not email or not message:
            return jsonify({"error": "All fields are required"}), 400

        # Save to database
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

if __name__ == '__main__':
    app.run(debug=True, port=5005)  # Running on port 5005
