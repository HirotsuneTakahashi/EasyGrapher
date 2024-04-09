import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .graph_method import bar,line,hist,box,area,pie,scatter
from flask_babel import get_locale
import shutil
from flask import current_app as app
from datetime import datetime
from flask import session

def graph(df):
    image_paths = {
    'bar': 'app/static/images/graph_bar.png',
    'line': 'app/static/images/graph_line.png',
    'hist': 'app/static/images/graph_hist.png',
    'box': 'app/static/images/graph_box.png',
    'area': 'app/static/images/graph_area.png',
    'pie': 'app/static/images/graph_pie.png',
    'scatter': 'app/static/images/graph_scatter.png'
    }

    error_image_paths = {
        'en': 'app/static/images/graph0_error_en.png',
        'ja': 'app/static/images/graph0_error_ja.png'  # 日本語のロケールコードは通常 'ja' です
    }

    results = {
        'bar': False,
        'line': False,
        'hist': False,
        'box': False,
        'area': False,
        'pie': False
    }

    graph_functions = {
        'bar': bar,
        'line': line,
        'hist': hist,
        'box': box,
        'area': area,
        'pie': pie,
        'scatter': scatter
    }

    current_locale = str(get_locale())
    error_image_path = error_image_paths.get(current_locale, 'app/static/images/graph0_error_en.png')  # デフォルトは英語

    results['bar'] = not bar(df) is None
    results['line'] = not line(df) is None
    results['hist'] = not hist(df) is None
    results['box'] = not box(df) is None
    results['area'] = not area(df) is None
    results['pie'] = not pie(df) is None
    results['scatter'] = not scatter(df) is None

    for graph_type, is_executable in results.items():
        if is_executable:  # 実行可能な場合
            func = graph_functions[graph_type]  # 対応する関数を取得
            func(df)
        else:  # 実行不可能な場合
            output_path = image_paths[graph_type]  # 出力画像ファイルのパスを取得
            shutil.copyfile(error_image_path, output_path)  # エラー画像で上書き
