from flask import Flask, request, render_template, jsonify, url_for
import requests

app = Flask(__name__)


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
    api_key = '67d3951e778decfbc3ce684fb106fe29'  # coloque sua chave real aqui
    weather_data = get_weather_data(city_name, api_key)
    return jsonify(weather_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
