from flask import Flask, render_template, request
from user import user
from sensor import sensor
from actuator import actuator

app = Flask(__name__)

app.register_blueprint(user, url_prefix = '/')
app.register_blueprint(sensor, url_prefix = '/')
app.register_blueprint(actuator, url_prefix = '/')

@app.route('/')
def index():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
