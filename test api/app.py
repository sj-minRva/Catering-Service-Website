from flask import Flask, request, jsonify
from flask_cors import CORS
from database import insert_customer

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/customers', methods=['POST'])
def create_customer():
    customer_data = request.json
    print('Received customer data:', customer_data)

    insert_customer(customer_data['name'], customer_data['email'], customer_data['password'])

    return jsonify({'message': 'Customer data received successfully', 'data': customer_data}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
