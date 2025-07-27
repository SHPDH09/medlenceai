from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Aiven MySQL DB credentials
db = pymysql.connect(
    host="mysql-e8883ac-raunakkumarjob-7886.i.aivencloud.com",
    user="avnadmin",
    password="AVNS_rFSiPQG-ybjDAzwlU6n",
    database="defaultdb",
    port=12637,
    ssl={'ssl': {}}
)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("fullname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("password")
    confirm = request.form.get("confirm_password")

    if password != confirm:
        return "Passwords do not match", 400

    role = "User"  # default role for every registration

    cursor = db.cursor()
    try:
        sql = "INSERT INTO users (name, email, phone, password, role) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (name, email, phone, password, role))
        db.commit()
        return "Registration successful", 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
