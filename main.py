from app import create_app
import webbrowser
import threading

def open_browser():
      #webbrowser.open_new('http://127.0.0.1:5000/?lang=ja')
      webbrowser.open_new('http://127.0.0.1:5000/?lang=en')

app = create_app()
app.config['UPLOAD_FOLDER'] = '.'  # アップロードされたファイルを保存するディレクトリ
app.config['PROCESSED_DATA_FOLDER'] = 'app/static/files'  # 処理後のデータを保存するディレクトリ

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True,
            #use_reloader=False
    )