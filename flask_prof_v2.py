from flask import Flask
from flask_profiler import Profiler

profiler = Profiler()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['flask_profiler'] = {
    "enabled" : app.config['DEBUG'],
    "storage" : {
        "engine" : "sqlite"
    },
    "basicAuth" : {
        "enabled" : True,
        "username" : "admin",
        "password" : "admin"
    }
}

profiler.init_app(app)


@app.route("/")
def index():
    return "Welcome to profiling!"


@app.route("/user/<name>")
def users(name):
    return f"The specified user is: {name}"

if __name__ == "__main__":
    app.run('0.0.0.0', debug= True)