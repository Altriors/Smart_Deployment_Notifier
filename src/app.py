from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "healthy",
        "message": "Smart Deployment Notifier is running successfully."
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/api/version')
def version():
    return jsonify({
        "version": "1.0.0",
        "app": "Smart Deployment Notifier"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
