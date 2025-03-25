from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)

# ✅ Allow all origins (temporary fix, can be restricted later)
CORS(app, resources={r"/api/*": {"origins": "*"}})

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        database="Catering",
        user="root",
        password="root"
    )

@app.route('/api/customers/<int:id>', methods=['OPTIONS', 'DELETE'])
def delete_customer(id):
    if request.method == 'OPTIONS':
        #Preflight request needs proper CORS headers
        response = jsonify({"message": "CORS preflight request success"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Methods", "DELETE, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return response, 200

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM bookings WHERE id = %s", (id,))  # ✅ Ensure the table name is correct
        conn.commit()
        cursor.close()
        conn.close()
        
        response = jsonify({"message": f"Customer {id} deleted successfully"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 200
    except mysql.connector.Error as err:
        response = jsonify({"error": str(err)})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
