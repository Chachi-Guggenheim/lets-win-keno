from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    n = int(data['number'])
    if n < 1 or n > 12:
        return jsonify({'error': 'Number must be between 1 and 12'}), 400
    random_numbers = random.sample(range(1, 81), n)
    return jsonify({'numbers': random_numbers})

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT from environment or default to 5000
    app.run(host='0.0.0.0', port=port)

