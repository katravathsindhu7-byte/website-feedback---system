from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

stored_otp = {}

@app.route("/")
def home():
    return render_template("feedback.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    email = data["email"]
    otp = "1279"

    stored_otp[email] = otp

    print("OTP SENT:", otp)

    return jsonify({"message": "OTP sent successfully", "status": "success"})

@app.route("/verify", methods=["POST"])
def verify():
    data = request.get_json()

    email = data["email"]
    otp = data["otp"]

    if email in stored_otp and stored_otp[email] == otp:
        return jsonify({"message": "OTP Verified Successfully"})
    else:
        return jsonify({"message": "Invalid OTP"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
