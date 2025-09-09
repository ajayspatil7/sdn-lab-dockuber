from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World from Docker Desktop Kubernetes!"

@app.route("/healthz")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    # Bind to all interfaces inside the container
    app.run(host="0.0.0.0", port=5000)
