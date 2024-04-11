import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from flask import session

def generate_base64_graph(graph_type):
    path = session.get('processed_file_path')
    df = pd.read_csv(path)
    if graph_type=="bar":

        # x軸の候補（カテゴリーまたは時系列データ）
        x_candidates = df.select_dtypes(include=['object', 'datetime']).columns.tolist()
        # y軸の候補（数値データ）
        y_candidates = df.select_dtypes(include=['number']).columns.tolist()
        
        x_axis = x_candidates[0] if x_candidates else None
        y_axis = y_candidates if y_candidates else None

        ax = df.plot(x=x_axis, y=y_axis, kind='bar', figsize=(10, 6))

        ax.set_title('日本語のタイトル')
        ax.set_xlabel('X軸ラベル')
        ax.set_ylabel('Y軸ラベル')

    elif graph_type=="line":
    
        # x軸の候補（カテゴリーまたは時系列データ）
        x_candidates = df.select_dtypes(include=['object', 'datetime']).columns.tolist()
        # y軸の候補（数値データ）
        y_candidates = df.select_dtypes(include=['number']).columns.tolist()
        
        x_axis = x_candidates[0] if x_candidates else None
        y_axis = y_candidates if y_candidates else None

        ax = df.plot(kind='line', figsize=(10, 6))

        ax.set_title('日本語のタイトル')
        ax.set_xlabel('X軸ラベル')
        ax.set_ylabel('Y軸ラベル')

    elif graph_type=="hist":
        numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
        column_to_plot = numeric_columns[0]
        data_to_plot = df[column_to_plot].dropna()

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.hist(data_to_plot, bins='auto')  # 'auto'でビンの数をデータに基づいて自動決定
        ax.set_title(f'ヒストグラム: {column_to_plot}')  # 修正箇所
        ax.set_xlabel(column_to_plot)  # 修正箇所
        ax.set_ylabel('頻度')  # 修正箇所

    elif graph_type=="box":
        numeric_candidates = df.select_dtypes(include=['number']).columns.tolist()
        ax = df[numeric_candidates].plot(kind='box', figsize=(10, 6))

        ax.set_title('箱ひげ図')
        ax.set_ylabel('値')

    elif graph_type=="area":
        numeric_candidates = df.select_dtypes(include=['number']).columns.tolist()
        ax = df[numeric_candidates].plot(kind='area', figsize=(10, 6), stacked=False)  # stacked=False で積み上げない面積グラフ

        ax.set_title('面積グラフ')
        ax.set_ylabel('値')
        ax.set_xlabel('インデックス（または時系列データ）')
        
    elif graph_type=="pie":
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

    elif graph_type=="scatter":
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

    # 画像をBase64エンコーディングして返す
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    base64_string = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    return base64_string

def customize_base64_graph(graphType, graph_title, x_column, y_column):
    path = session.get('processed_file_path')
    df = pd.read_csv(path)
    if graphType=="bar":
        
        # x軸の候補（カテゴリーまたは時系列データ）
        x_candidates = df.select_dtypes(include=['object', 'datetime']).columns.tolist()
        # y軸の候補（数値データ）
        y_candidates = df.select_dtypes(include=['number']).columns.tolist()
        
        x_axis = x_candidates[0] if x_candidates else None
        y_axis = y_candidates if y_candidates else None

        ax = df.plot(x=x_axis, y=y_axis, kind='bar', figsize=(10, 6))

        ax.set_title('日本語のタイトル')
        ax.set_xlabel('X軸ラベル')
        ax.set_ylabel('Y軸ラベル')

    elif graphType=="line":
    
        # x軸の候補（カテゴリーまたは時系列データ）
        x_candidates = df.select_dtypes(include=['object', 'datetime']).columns.tolist()
        # y軸の候補（数値データ）
        y_candidates = df.select_dtypes(include=['number']).columns.tolist()
        
        x_axis = x_candidates[0] if x_candidates else None
        y_axis = y_candidates if y_candidates else None

        ax = df.plot(kind='line', figsize=(10, 6))

        ax.set_title('日本語のタイトル')
        ax.set_xlabel('X軸ラベル')
        ax.set_ylabel('Y軸ラベル')

    elif graphType=="hist":
        numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
        column_to_plot = numeric_columns[0]
        data_to_plot = df[column_to_plot].dropna()

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.hist(data_to_plot, bins='auto')  # 'auto'でビンの数をデータに基づいて自動決定
        ax.set_title(f'ヒストグラム: {column_to_plot}')  # 修正箇所
        ax.set_xlabel(column_to_plot)  # 修正箇所
        ax.set_ylabel('頻度')  # 修正箇所

    elif graphType=="box":
        numeric_candidates = df.select_dtypes(include=['number']).columns.tolist()
        ax = df[numeric_candidates].plot(kind='box', figsize=(10, 6))

        ax.set_title('箱ひげ図')
        ax.set_ylabel('値')

    elif graphType=="area":
        numeric_candidates = df.select_dtypes(include=['number']).columns.tolist()
        ax = df[numeric_candidates].plot(kind='area', figsize=(10, 6), stacked=False)  # stacked=False で積み上げない面積グラフ

        ax.set_title('面積グラフ')
        ax.set_ylabel('値')
        ax.set_xlabel('インデックス（または時系列データ）')
        
    elif graphType=="pie":
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

    elif graphType=="scatter":
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

    ax.set_title(graph_title)
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)

    # 画像をBase64エンコーディングして返す
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    base64_custom = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    return base64_custom