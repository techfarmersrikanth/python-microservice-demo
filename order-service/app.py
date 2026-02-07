from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/orders")
def get_orders():
    # Call user-service using Docker service name
    response = requests.get("http://user-service:5000/users")
    users = response.json()

    return jsonify({
        "message": "Orders fetched successfully",
        "users_from_user_service": users
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
