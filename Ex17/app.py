from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to My Flask API"

@app.route("/student")
def student():
    return "Name: Rashmi"

@app.route("/college")
def college():
    return "ABC Engineering College"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)