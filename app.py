from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual Make.com webhook URL
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/29t2vbq1flngv5amko8ukrgyibjr6ps3"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = {
        "name": request.form.get('name'),
        "email": request.form.get('email'),
        "phone": request.form.get('phone', ''),
        "message": request.form.get('message'),
    }
    try:
        response = requests.post(MAKE_WEBHOOK_URL, json=data, timeout=10)
        return jsonify({"status": "success", "message": "Message sent successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)