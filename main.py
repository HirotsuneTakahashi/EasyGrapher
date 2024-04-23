from app import create_app
import webbrowser
import threading
import os
from apscheduler.schedulers.background import BackgroundScheduler
import glob
from datetime import datetime, timedelta

def delete_files():
    """アップロードディレクトリと処理後データディレクトリ内のファイルをすべて削除"""
    # アップロードされたファイルの削除
    upload_files = glob.glob(os.path.join(app.config['UPLOAD_FOLDER'], '*'))
    for file in upload_files:
        os.remove(file)

    # 処理後のデータファイルの削除
    processed_files = glob.glob(os.path.join(app.config['PROCESSED_DATA_FOLDER'], '*'))
    for file in processed_files:
        os.remove(file)

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/?lang=ja')
      #webbrowser.open_new('http://127.0.0.1:5000/?lang=en')

app = create_app()
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')  # アップロードされたファイルを保存するディレクトリ
app.config['PROCESSED_DATA_FOLDER'] = os.path.join(os.getcwd(), 'uploads')# 処理後のデータを保存するディレクトリ
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MBの最大サイズ

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_DATA_FOLDER'], exist_ok=True)

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(delete_files, 'date', run_date=datetime.now() + timedelta(hours=1))

if __name__ == '__main__':
    #threading.Timer(1.25, open_browser).start()
    app.run(debug=True,
            #use_reloader=False
    )