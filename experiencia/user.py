from flask import Blueprint, request, render_template

user = Blueprint("user", __name__, template_folder="templates")

users = {
    "user1" : "1234",
    "user2" : "1234"
}

sensores = ["dht", "sensor de movimento", "sensor de luminosidade"]
atuadores = ["servo", "led", "buzzer"]

@user.route('/')
def index():
    return render_template("home.html")

@user.route('/sensors')
def sensors():
    global sensores
    return render_template("sensors.html", devices=sensores)


@user.route('/validated_user', methods=['GET', 'POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if user in users and user[user] == password:
            return render_template("home.html")
        else:
            render_template("login.html")

@user.route('/register_user')
def register_user():
    return render_template("register_user.html")

@user.route('/list_users')
def list_users():
    global users
    return render_template("users.html", devices=users)


@user.route('/add_user', methods=['POST'])
def add_user():  
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)

    users[user] = password
    return render_template("users.html", devices=users)

@user.route('/remove_user')
def remove_user():
    global users
    return render_template("remove_user.html", devices=users)

@user.route('/del_user', methods=['GET', 'POST'])
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)
    users.pop(user)
    return render_template('users.html', devices=users)
