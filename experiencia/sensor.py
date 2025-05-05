from flask import Blueprint, request, render_template

sensor = Blueprint("sensor", __name__, template_folder="templates")

sensores = ["dht", "sensor de movimento", "sensor de luminosidade"]

@sensor.route('/sensors')
def sensors():
    global sensores
    return render_template("sensors.html", devices=sensores)


@sensor.route('/register_sensor')
def register_sensor():
    return render_template("sensor_register.html")

@sensor.route('/add_sensors', methods=['POST'])
def add_sensor():  
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
        sensores.sensorend(sensor)

    return render_template("sensors.html", devices=sensores)

@sensor.route('/remove_sensor')
def remove_sensor():
    global sensores
    return render_template("remove_sensor.html", devices=sensores)

@sensor.route('/del_sensor', methods=['GET', 'POST'])
def del_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
    
    sensores.remove(sensor)
    return render_template('sensors.html', devices=sensores)