from flask import Flask, render_template, request, jsonify
from flask import current_app as app
from .graph import graph
from .graph_cutomize import generate_base64_graph, customize_base64_graph
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from datetime import datetime
from flask import session
import uuid
from werkzeug.utils import secure_filename
from flask_babel import get_locale

def init_app(app):
    @app.route('/')
    def home():
        return render_template('01_home.html', locale=get_locale())

    @app.route('/loading')
    def loading():
        return render_template('02_loading.html', locale=get_locale())

    @app.route('/select')
    def select():
        return render_template('03_select.html', locale=get_locale())

    @app.route('/answer')
    def answer():
        return render_template('04_answer.html', locale=get_locale())  
    
    @app.route('/howToUse')
    def howToUse():
        next_page = request.args.get('next', None)
        #↑ボタンをHomeに変更するためのコマンド
        return render_template('81_howToUse.html', next=next_page, locale=get_locale())
    
    @app.route('/termsOfUse')
    def termsOfUse():
        next_page = request.args.get('next', None)
        #↑ボタンをHomeに変更するためのコマンド
        return render_template('82_termsOfUse.html', next=next_page, locale=get_locale())
    
    @app.route('/aboutThisSite')
    def aboutThisSite():
        next_page = request.args.get('next', None)
        #↑ボタンをHomeに変更するためのコマンド
        return render_template('83_aboutThisSite.html', next=next_page, locale=get_locale())
    
    @app.route('/privacyPolicy')
    def privacyPolicy():
        next_page = request.args.get('next', None)
        #↑ボタンをHomeに変更するためのコマンド
        return render_template('84_privacyPolicy.html', next=next_page, locale=get_locale())
    
    @app.route('/faq')
    def faq():
        next_page = request.args.get('next', None)
        #↑ボタンをHomeに変更するためのコマンド
        return render_template('85_faq.html', next=next_page, locale=get_locale())
    
    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            file = request.files['file']

            filename = file.filename
            _, ext = os.path.splitext(filename)

            random_filename = f"{uuid.uuid4().hex}{ext}"

            if ext in ['.xls', '.xlsx']:

                file_path = os.path.join(app.config['UPLOAD_FOLDER'], random_filename)
                file.save(file_path)

                df = pd.read_excel(file)  # アップロードされたファイルを読み込む
                processed_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}.csv"
                processed_file_path = os.path.join(app.config['PROCESSED_DATA_FOLDER'], processed_filename)
                df.to_csv(processed_file_path, index=False)
                session['processed_file_path'] = processed_file_path
                os.remove(file_path)
                graph(df)
    
        return render_template('03_select.html', locale=get_locale())
    
    @app.route('/selectImage', methods=['POST'])
    def selectImage():
        if request.method == 'POST':
            # リクエストからデータを取得
            action = request.form['action']
            base64_graph = generate_base64_graph(action)
            return render_template('04_answer.html', img_data=base64_graph, graph_type=action, locale=get_locale())
        
    @app.route('/customizeGraph', methods=['POST'])
    def customizeGraph():
        # リクエストからパラメータを取得
        data = request.json
        graphType = data['graph_type']
        graph_title = data['graph_title']
        x_column = data['x_column']
        y_column = data['y_column']
        
        base64_string = customize_base64_graph(graphType, graph_title, x_column, y_column)
        
        # Base64エンコーディングされた画像データを返す
        return jsonify({'img_data': base64_string})