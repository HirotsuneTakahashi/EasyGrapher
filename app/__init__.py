from flask import Flask, request, g
from flask_babel import Babel
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # get_locale関数を定義
    def get_locale():
        # リクエストの引数から言語設定を取得し、なければデフォルトの言語設定を使用
        return request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])


    # Babelインスタンスを作成し、locale_selectorパラメータにget_locale関数を渡す
    babel = Babel(app, locale_selector=get_locale)

    # get_locale関数をテンプレートのグローバル関数として登録
    @app.context_processor
    def context_processor():
        return dict(get_locale=get_locale)

    from . import routes
    routes.init_app(app)
    
    return app