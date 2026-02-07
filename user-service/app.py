from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def get_users():
    return jsonify(["Ravi", "Sita", "John"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
