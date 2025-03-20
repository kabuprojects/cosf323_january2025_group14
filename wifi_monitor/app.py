from flask import Flask, render_template, jsonify
from wifi_scanner import scan_wifi  

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Loads the frontend

@app.route("/scan")
def scan():
    return jsonify(scan_wifi())  # Calls scan_wifi() and returns results in JSON format

if __name__ == "__main__":
    app.run(debug=True)
