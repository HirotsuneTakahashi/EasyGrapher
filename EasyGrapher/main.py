from app import create_app
import webbrowser
import threading

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/?lang=ja')
      #webbrowser.open_new('http://127.0.0.1:5000/?lang=en')

app = create_app()

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True,use_reloader=False)