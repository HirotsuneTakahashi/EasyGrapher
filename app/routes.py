from flask import render_template
from flask import current_app as app

def init_app(app):
    @app.route('/')
    def home():
        return render_template('01_home.html')

    @app.route('/loading')
    def loading():
        return render_template('02_loading.html')

    @app.route('/select')
    def select():
        return render_template('03_select.html')

    @app.route('/answer')
    def answer():
        return render_template('04_answer.html')  