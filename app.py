from datetime import datetime
import sqlite3
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.secret_key = 'jnv_secret_key'


def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            password TEXT
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS access_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        material TEXT,
        access_time TEXT
    )
''')

    conn.commit()
    conn.close()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            session['email'] = email
            return redirect(url_for('materials'))
        else:
            return "Invalid Credentials!"

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()

        return "Registered Successfully!"

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('home'))


@app.route('/materials')
def materials():
    if 'email' in session:

        email = session['email']
        material = "JNV Study Materials"
        access_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO access_log (email, material, access_time) VALUES (?, ?, ?)",
                       (email, material, access_time))
        conn.commit()
        conn.close()

        return render_template('materials.html', email=email)
    else:
        return redirect(url_for('login'))


@app.route('/admin_logs')
def admin_logs():

    if 'email' in session and session['email'] == "admin@jnv.com":

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT email, material, access_time FROM access_log")
        logs = cursor.fetchall()

        conn.close()

        return render_template('admin_logs.html', logs=logs)

    else:
        return "Access Denied!"


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
