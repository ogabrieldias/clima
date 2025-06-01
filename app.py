from flask import Flask, request, render_template, jsonify
import requests
import os

app = Flask(__name__)

# Pega a chave da API do ambiente (variável OPENWEATHER_API_KEY)
API_KEY = os.environ.get('OPENWEATHER_API_KEY')

def get_weather_data(city_name, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}&lang=pt_br'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city_name = request.json['city']
    if not API_KEY:
        return jsonify({"error": "API key not configured"}), 500
    weather_data = get_weather_data(city_name, API_KEY)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
