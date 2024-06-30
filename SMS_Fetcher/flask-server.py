import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

AlgolabSifre = 0

@app.route('/send_message', methods=['POST'])
def send_message():
    
    global AlgolabSifre
    try:
        data = request.get_json()
        
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        message = data.get('message')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        with open('messages.txt', 'r') as f:
            lines = f.readlines()
        
        lines[0] = message
        
        with open('messages.txt', 'w') as f:
            f.writelines(lines)
        
        AlgolabSifre = message
        
        return jsonify({'status': 'success', 'message': message}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_algolab_sms', methods=['GET'])
def algolab():
    
    with open('messages.txt', 'r') as f:
        lines = f.readlines()
        
    sifre = lines[0].strip() if lines else ""
    
    if lines:
        lines[0] = "0"
        
    with open('messages.txt', 'w') as f:
        f.writelines(lines)
    
    return sifre    
    
    
if __name__ == '__main__':
    app.run(host='4----------', port=7000)
