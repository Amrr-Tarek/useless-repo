from flask import Flask, jsonify

app = Flask(__name__)

API_KEY = "12345-SUPER-SECRET-PLAINTEXT-KEY"

@app.route("/")
def home():
    return jsonify(status="success", message="Hello, CI/CD!")

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":  # pragma: no cover
    app.run(host="127.0.0.1", port=5000)
