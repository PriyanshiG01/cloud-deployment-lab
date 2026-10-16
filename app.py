
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head><title>Cloud Deployment Lab</title></head>
      <body style="font-family: Arial; text-align: center; margin-top: 100px;">
        <h1>Welcome to My Cloud Application!</h1>
        <h2>Name: Priyanshi</h2>
        <h3>Application Version: 1.0.0</h3>
        <p>Successfully deployed using Docker and AWS EC2.</p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy", version="1.0.0")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
