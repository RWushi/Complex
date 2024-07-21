from flask import render_template, request, session, jsonify
from Weather import geocode_city as gc, get_weather as gw
from History import update_history as uh, get_history as gh
from Config import app


@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        coords = gc(city)
        if coords:
            weather_data = gw(coords)
            session['last_city'] = city
            uh(city)
        else:
            weather_data = None
        return render_template('result.html', city=city, weather=weather_data)

    last_city = session.get('last_city', None)
    return render_template('city.html', last_city=last_city)


@app.route('/history', methods=['GET'])
def send_history():
    history = gh()
    return jsonify(history)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
