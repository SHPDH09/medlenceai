from flask import Flask, request, redirect, render_template, flash, url_for, session
import pymysql

app = Flask(__name__)
app.secret_key = 'e1f7c6a4b2f84331ad0c9ff84e20b7d1'

# Database connection
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
            flash("Passwords do not match", "error")
            return redirect("/register")

        cursor = db.cursor()
        try:
            sql = "INSERT INTO users (name, email, phone, password, role) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, email, phone, password, "user"))  # default role
            db.commit()
            session['username'] = name
            return redirect("/success")
        except Exception as e:
            flash("Error: " + str(e), "error")
            return redirect("/register")

    return render_template("register.html")

@app.route("/success")
def success():
    username = session.get('username', 'User')
    return f"""
    <h2 style='text-align:center;margin-top:50px;color:green;'>Registration Successful 🎉</h2>
    <p style='text-align:center;'>Welcome, <strong>{username}</strong>!</p>
    <p style='text-align:center;'><a href='/login'>Click here to login</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)
