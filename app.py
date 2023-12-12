from flask import Flask, request, jsonify

app = Flask(__name__)

GRAVITY = {
    'MERCURY': 3.7,
    'VENUS': 8.87,
    'EARTH': 9.81,
    'MARS': 3.721,
    'JUPITER': 24.79,
    'SATURN': 10.44,
    'URANUS': 8.69,
    'NEPTUNE': 11.15
}

@app.route('/calculate_weight', methods=['POST'])
def calculate_weight():
    data = request.get_json()
    weight_on_earth = data.get('weight_on_earth')
    planet = data.get('planet').upper()

    if planet not in GRAVITY:
        return jsonify({'error': 'Invalid planet'}), 400
    earth_weight = weight_on_earth * GRAVITY['EARTH']
    weight_on_planet = earth_weight / GRAVITY[planet]
    return jsonify({'weight_on_planet': round(weight_on_planet, 5)})

if __name__ == '__main__':
    app.run(debug=True)
