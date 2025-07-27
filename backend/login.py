from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="mysql-e8883ac-raunakkumarjob-7886.i.aivencloud.com",
    port=12637,
    user="avnadmin",
    password="AVNS_rFSiPQG-ybjDAzwlU6n",
    database="defaultdb",
    ssl_disabled=False
)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"status": "fail", "message": "Email and Password required"}), 400

    cursor = db.cursor()
    query = "SELECT * FROM users WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()

    if result:
        return jsonify({"status": "success", "message": "Login successful"})
    else:
        return jsonify({"status": "fail", "message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
