import sqlite3
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------------- DATABASE SETUP ----------------
def init_db():
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("feedback.html")

# ---------------- SUBMIT FEEDBACK ----------------
@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    email = data["email"]
    message = data["message"]

    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("INSERT INTO feedback (email, message) VALUES (?, ?)", (email, message))
    conn.commit()
    conn.close()

    return jsonify({"message": "Feedback submitted successfully"})

# ---------------- VIEW ALL FEEDBACK (ADMIN) ----------------
@app.route("/feedbacks", methods=["GET"])
def feedbacks():
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("SELECT * FROM feedback")
    data = c.fetchall()
    conn.close()

    return jsonify(data)

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
