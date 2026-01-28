from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app)  # Важно: разрешает браузеру отправлять данные на сервер

# Маршрут: открывает твой HTML файл
@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

# Маршрут: принимает данные от формы


if __name__ == '__main__':
    print("Сервер запущен! Перейди по адресу: http://0.0.0.0:8000")
    app.run(port=8000)
