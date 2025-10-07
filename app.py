import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Ceremainet server is running."

@app.get("/c/<cid>")
def cert(cid):
    return jsonify({"certificate": cid, "status": "placeholder"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
