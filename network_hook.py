from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data and 'text' in data:
        # Trigger agy command with the text received from the network
        result = subprocess.run(['agy', '-p', data['text']], capture_output=True, text=True)
        return jsonify({'status': 'success', 'output': result.stdout.strip()})
    return jsonify({'status': 'error', 'message': 'No text provided'}), 400

if __name__ == '__main__':
    # Listen on all interfaces to allow local network devices (or SMS gateways) to hook in
    app.run(host='0.0.0.0', port=5000)
