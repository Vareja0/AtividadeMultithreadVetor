from flask import Blueprint, request, render_template

actuator = Blueprint("actuator", __name__, template_folder="templates")

atuadores = ["servo", "led", "buzzer"]

@actuator.route('/actuators')
def actuators():
    global atuadores
    return render_template("actuators.html", devices=atuadores)

@actuator.route("/register_actuator")
def actuador_register():
    return render_template("atuador_register.html")

@actuator.route('/add_atuador', methods=['POST'])
def add_atuador():  
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
        atuadores.actuatorend(atuador)

    return render_template("actuators.html", devices=atuadores)

@actuator.route('/remove_actuator')
def remove_actuator():
    global atuadores
    return render_template("remove_actuator.html", devices=atuadores)

@actuator.route('/del_actuator', methods=['GET', 'POST'])
def del_actuator():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
    
    atuadores.remove(atuador)
    return render_template('actuators.html', devices=atuadores)