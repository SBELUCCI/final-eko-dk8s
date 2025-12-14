from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_URL = "http://api:8000/items"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
    response = requests.get(API_URL)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)