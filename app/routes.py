from flask import Flask, render_template, request
from flask import current_app as app
from .graph import graph
from .graph_cutomize import generate_base64_graph
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from datetime import datetime
from flask import session

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
    
    @app.route('/howToUse')
    def howToUse():
        next_page = request.args.get('next', None)
        #↑ボタンをHomeに変更するためのコマンド
        return render_template('81_howToUse.html', next=next_page)
    
    @app.route('/termsOfUse')
    def termsOfUse():
        next_page = request.args.get('next', None)
        #↑ボタンをHomeに変更するためのコマンド
        return render_template('82_termsOfUse.html', next=next_page)
    
    @app.route('/aboutThisSite')
    def aboutThisSite():
        next_page = request.args.get('next', None)
        #↑ボタンをHomeに変更するためのコマンド
        return render_template('83_aboutThisSite.html', next=next_page)
    
    @app.route('/faq')
    def faq():
        next_page = request.args.get('next', None)
        #↑ボタンをHomeに変更するためのコマンド
        return render_template('84_faq.html', next=next_page)
    
    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            file = request.files['file']

            filename = file.filename
            _, ext = os.path.splitext(filename)

            if ext in ['.xls', '.xlsx']:
                df = pd.read_excel(file)  # アップロードされたファイルを読み込む
                processed_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}.csv"
                processed_file_path = os.path.join(app.config['PROCESSED_DATA_FOLDER'], processed_filename)
                df.to_csv(processed_file_path, index=False)
                session['processed_file_path'] = processed_file_path
                graph(df)

        return render_template('03_select.html')
    
    @app.route('/selectImage', methods=['POST'])
    def selectImage():
        if request.method == 'POST':
            # リクエストからデータを取得
            action = request.form['action']
            base64_graph = generate_base64_graph(action)
            return render_template('04_answer.html', img_data=base64_graph)