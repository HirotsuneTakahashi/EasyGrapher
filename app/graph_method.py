import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def bar(df): 
    # x軸の候補（カテゴリーまたは時系列データ）
    x_candidates = df.select_dtypes(include=['object', 'datetime']).columns.tolist()
    # y軸の候補（数値データ）
    y_candidates = df.select_dtypes(include=['number']).columns.tolist()
    
    x_axis = x_candidates[0] if x_candidates else None
    y_axis = y_candidates if y_candidates else None

    ax = df.plot(x=x_axis, y=y_axis, kind='bar')
    image_path = 'app/static/images/graph_bar.png'  # 静的ファイルを保存するパスを指定
    plt.savefig(image_path)
    plt.close()  # 画像を保存した後は閉じます

def line(df):

    # x軸の候補（カテゴリーまたは時系列データ）
    x_candidates = df.select_dtypes(include=['object', 'datetime']).columns.tolist()
    # y軸の候補（数値データ）
    y_candidates = df.select_dtypes(include=['number']).columns.tolist()
    
    x_axis = x_candidates[0] if x_candidates else None
    y_axis = y_candidates if y_candidates else None
    
    ax = df.plot(kind='line')
    image_path = 'app/static/images/graph_line.png'
    plt.savefig(image_path)
    plt.close()

def hist(df):
    ax = df.plot(kind='hist')
    image_path = 'app/static/images/graph_hist.png'
    plt.savefig(image_path)
    plt.close()

def box(df):
    ax = df.plot(kind='box')
    image_path = 'app/static/images/graph_box.png'
    plt.savefig(image_path)
    plt.close()

def area(df):
    ax = df.plot(kind='area')
    image_path = 'app/static/images/graph_area.png'
    plt.savefig(image_path)
    plt.close()

def pie(df):
    ax = df.plot(kind='pie')
    image_path = 'app/static/images/graph_pie.png'
    plt.savefig(image_path)
    plt.close()

def scatter(df):
    ax = df.plot(kind='scatter')
    image_path = 'app/static/images/graph_scatter.png'
    plt.savefig(image_path)
    plt.close()