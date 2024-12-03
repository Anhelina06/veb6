from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

# Ініціалізація файлу, якщо не існує
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# Ендпойнт для збереження даних
@app.route('/save', methods=['POST'])
def save_data():
    try:
        data = request.json
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f)
        return jsonify({"message": "Data saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ендпойнт для отримання даних
@app.route('/load', methods=['GET'])
def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Запуск серверу
if __name__ == '__main__':
    app.run(debug=True)
