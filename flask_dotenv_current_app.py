from flask_dotenv import DotEnv
from flask import Flask, current_app

env.init_app(app, env_file = '.env', verbose_mode = True)

@app.route('/')
def index():
        return f"DBUSER is {current_app.config['DBUSER']}, DBPASS is {current_app.config['DBPASS']}, DBSERVER is {current_app.config['DBSERVER']}, DBASE is {current_app.config['DBASE']}"

if __name__ == '__main__':
        app.run('0.0.0.0',debug = True)
