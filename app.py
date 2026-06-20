import sqlite3
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("feedback.html")

# ---------------- SUBMIT ----------------
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

    return jsonify({"message": "Feedback saved successfully"})

# ---------------- ADMIN DASHBOARD ----------------
@app.route("/admin")
def admin():
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("SELECT * FROM feedback")
    data = c.fetchall()
    conn.close()

    return render_template("admin.html", feedbacks=data)

# ---------------- DELETE FEEDBACK ----------------
@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("DELETE FROM feedback WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return "<script>alert('Deleted successfully');window.location='/admin';</script>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
