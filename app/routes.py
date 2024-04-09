from flask import Flask, render_template, request, jsonify
from flask import current_app as app
from .graph import graph
from .graph_cutomize import generate_base64_graph
from flask import session
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
            app.config['UPLOAD_FOLDER'] = '.'  # アップロードされたファイルを保存するディレクトリ
            app.config['PROCESSED_DATA_FOLDER'] = 'app/static/files'  # 処理後のデータを保存するディレクトリ
            app.secret_key = 'f9b61bc784fb6b74ac772a2fcefd76cd24e2fa5f8332f820'

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
        # リクエストからデータを取得
        data = request.json
        graph_type = data['graph_type']
        processed_file_path = session.get('processed_file_path')
        if processed_file_path:
            # graph 関数を呼び出し、ファイルパスを渡す
            base64_graph = generate_base64_graph(graph_type, processed_file_path)
            return jsonify({'success': True, 'image': base64_graph})
        else:
            #  エラーハンドリング
            return jsonify({'error': 'Processed file not found'}), 404