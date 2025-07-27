from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'e1f7c6a4b2f84331ad0c9ff84e20b7d1'  # Use a secure, randomly generated key in production

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
            return "All fields are required."

        if password != confirm_password:
            return "Passwords do not match."

        hashed_password = generate_password_hash(password)

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if email already exists
            cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                return "Email already registered."

            insert_query = """
                INSERT INTO users (name, email, phone, password, role)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (name, email, phone, hashed_password, "user"))
            conn.commit()

            session["username"] = name
            return redirect(url_for("success"))

        except Exception as e:
            return f"Database error: {str(e)}"

        finally:
            cursor.close()
            conn.close()

    return render_template("register.html")  # Make sure this file is in the 'templates/' folder

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
