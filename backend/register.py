
from flask import Flask, render_template, request, redirect, flash, url_for, session
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = 'e1f7c6a4b2f84331ad0c9ff84e20b7d1'
# Database connection
def get_db_connection():
    return pymysql.connect(
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
        confirm_password = request.form.get("confirm_password")

        if not all([name, email, phone, password, confirm_password]):
            flash("Please fill out all fields.", "error")
            return redirect(url_for("register"))

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if email already exists
            cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                flash("Email is already registered.", "error")
                return redirect(url_for("register"))

            insert_query = """
                INSERT INTO users (name, email, phone, password, role)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (name, email, phone, hashed_password, "user"))
            conn.commit()

            session["username"] = name
            flash("Registration successful!", "success")
            return redirect(url_for("success"))

        except Exception as e:
            flash(f"Database error: {str(e)}", "error")
            return redirect(url_for("register"))

        finally:
            cursor.close()
            conn.close()

    return render_template("templates/register.html")



@app.route("/success")
def success():
    username = session.get("username", "User")
    return f"""
    <h2 style='text-align:center;margin-top:50px;color:green;'>Registration Successful 🎉</h2>
    <p style='text-align:center;'>Welcome, <strong>{username}</strong>!</p>
    <p style='text-align:center;'><a href='/login'>Click here to login</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)

