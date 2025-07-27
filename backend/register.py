from flask import Flask, request, redirect, render_template, flash, url_for
import pymysql

app = Flask(__name__)
app.secret_key = 'e1f7c6a4b2f84331ad0c9ff84e20b7d1'
  # Required for flash messages

# DB Connection
db = pymysql.connect(
    host="mysql-e8883ac-raunakkumarjob-7886.i.aivencloud.com",
    user="avnadmin",
    password="AVNS_rFSiPQG-ybjDAzwlU6n",
    database="defaultdb",
    port=12637,
    ssl={"ssl": {}}
)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("fullname")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        if password != confirm:
            return "Passwords do not match", 400

        cursor = db.cursor()
        try:
            sql = "INSERT INTO users (name, email, phone, password, role) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, email, phone, password, "user"))  # default role = user
            db.commit()
            return redirect("/success")  # redirect after successful register
        except Exception as e:
            return str(e), 500

    return render_template("register.html")

@app.route("/success")
def success():
    return "<h2 style='text-align:center;margin-top:50px;color:green;'>Registration Successful 🎉</h2><p style='text-align:center;'><a href='/login'>Click here to login</a></p>"

