from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/book', methods=['POST'])
def book_event():
    data = request.json  # Extract JSON data from request
    if not data:
        return jsonify({"error": "No data received"}), 400
    
    print("Received Booking Data:", data)

    return jsonify({"message": "Booking successful!", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
