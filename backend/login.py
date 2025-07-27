from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        conn = mysql.connector.connect(
            host="your-db-host",
            user="your-db-user",
            password="your-db-password",
            database="your-db-name"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        
        if user:
            return "Login Successful"
        else:
            return "Invalid email or password"
        
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run()
