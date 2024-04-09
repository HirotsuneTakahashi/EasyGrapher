import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#font_path = 'app/static/fonts/NotoSansJP-VariableFont_wght.ttf'  # フォントファイルのパス
#font_prop = FontProperties(fname=font_path)
plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'

def bar(df): 
    if not df.select_dtypes(include=['object', 'datetime']).columns.tolist() or not df.select_dtypes(include=['number']).columns.tolist():
        return None
    
    # x軸の候補（カテゴリーまたは時系列データ）
    x_candidates = df.select_dtypes(include=['object', 'datetime']).columns.tolist()
    # y軸の候補（数値データ）
    y_candidates = df.select_dtypes(include=['number']).columns.tolist()
    
    x_axis = x_candidates[0] if x_candidates else None
    y_axis = y_candidates if y_candidates else None

    ax = df.plot(x=x_axis, y=y_axis, kind='bar', figsize=(10, 6))
    image_path = 'app/static/images/graph_bar.png'  # 静的ファイルを保存するパスを指定

    ax.set_title('日本語のタイトル')
    ax.set_xlabel('X軸ラベル')
    ax.set_ylabel('Y軸ラベル')

    plt.savefig(image_path)
    plt.close()  # 画像を保存した後は閉じます
    return True

def line(df):
    if not df.select_dtypes(include=['object', 'datetime']).columns.tolist() or not df.select_dtypes(include=['number']).columns.tolist():
        return None
    
    # x軸の候補（カテゴリーまたは時系列データ）
    x_candidates = df.select_dtypes(include=['object', 'datetime']).columns.tolist()
    # y軸の候補（数値データ）
    y_candidates = df.select_dtypes(include=['number']).columns.tolist()
    
    x_axis = x_candidates[0] if x_candidates else None
    y_axis = y_candidates if y_candidates else None

    ax = df.plot(kind='line', figsize=(10, 6))
    image_path = 'app/static/images/graph_line.png'

    ax.set_title('日本語のタイトル')
    ax.set_xlabel('X軸ラベル')
    ax.set_ylabel('Y軸ラベル')

    plt.savefig(image_path)
    plt.close()
    return True

def hist(df):
    if not df.select_dtypes(include=['number']).columns.tolist():
        return None
    
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    column_to_plot = numeric_columns[0]
    data_to_plot = df[column_to_plot].dropna()

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.hist(data_to_plot, bins='auto')  # 'auto'でビンの数をデータに基づいて自動決定
    ax.set_title(f'ヒストグラム: {column_to_plot}')  # 修正箇所
    ax.set_xlabel(column_to_plot)  # 修正箇所
    ax.set_ylabel('頻度')  # 修正箇所

    image_path = 'app/static/images/graph_hist.png'
    plt.savefig(image_path)
    plt.close()
    return True

def box(df):
    if not df.select_dtypes(include=['number']).columns.tolist():
        return None
    numeric_candidates = df.select_dtypes(include=['number']).columns.tolist()
    ax = df[numeric_candidates].plot(kind='box', figsize=(10, 6))

    ax.set_title('箱ひげ図')
    ax.set_ylabel('値')
    
    image_path = 'app/static/images/graph_box.png'
    plt.savefig(image_path)
    plt.close()
    return True

def area(df):
    if not df.select_dtypes(include=['number']).columns.tolist():
        return None
    numeric_candidates = df.select_dtypes(include=['number']).columns.tolist()
    ax = df[numeric_candidates].plot(kind='area', figsize=(10, 6), stacked=False)  # stacked=False で積み上げない面積グラフ

    ax.set_title('面積グラフ')
    ax.set_ylabel('値')
    ax.set_xlabel('インデックス（または時系列データ）')
    
    image_path = 'app/static/images/graph_area.png'
    plt.savefig(image_path)
    plt.close()
    return True

def pie(df):
    category_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    if not category_columns or not numeric_columns:
        return None
    category_column = category_columns[0]
    value_column = numeric_columns[0]

    data = df.groupby(category_column)[value_column].sum()
    total = data.sum()
    proportions = data / total * 100

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(proportions, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.savefig('app/static/images/graph_pie.png')
    plt.close()
    return True

def scatter(df):
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    if len(numeric_columns) < 2:
        return None
    x_column = numeric_columns[0]
    y_column = numeric_columns[1]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df[x_column], df[y_column])
    ax.set_title(f'散布図: {x_column} vs {y_column}')  # axオブジェクトのset_メソッドを使用
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    plt.savefig('app/static/images/graph_scatter.png')
    plt.close()
    return True