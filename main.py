from flask import Flask, render_template, request
from weather import get_current_weather

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    units = request.args.get('units')  # Retrieve selected unit system

    if not bool(city.strip()):
        city = "Miami"

    # Pass units to get_current_weather
    weather_data = get_current_weather(city, units)

    # Check if 'cod' exists and is 200
    if 'cod' not in weather_data or weather_data['cod'] != 200:
        return render_template('city-not-found.html')

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
