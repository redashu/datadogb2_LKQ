from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging to a file
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    app.logger.info('Home page was accessed')
    return "Welcome to the Flask App!"

@app.route('/log', methods=['POST'])
def log_message():
    data = request.json
    message = data.get('message', 'No message provided')
    app.logger.info(f'Log message received: {message}')
    return jsonify({"status": "Message logged"}), 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)