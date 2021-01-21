from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/pyengine"
db = SQLAlchemy(app)


class tools(db.Model):
        Solution = db.Column(db.VARCHAR, primary_key = True)
        TaskList = db.Column(db.VARCHAR)
        TaskPath = db.Column(db.VARCHAR)

@app.route("/")
def index():
        Solutions = tools.query.all()
        print(Solutions)
        return render_template('index.html', solutions = Solutions)

if __name__ == "__main__":
        app.run(host="0.0.0.0", port = 8000, debug = True)