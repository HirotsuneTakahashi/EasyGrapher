import os
from docx import Document
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def graph(uploaded_file):
    filename = uploaded_file.filename
    _, ext = os.path.splitext(filename)
    
    if ext in ['.doc', '.docx']:
        document = Document(uploaded_file.stream)  # ファイルストリームからDocumentを読み込む
        table = document.tables[0]  # 最初のテーブルを取得
        data = []
        for row in table.rows:
            row_data = [cell.text for cell in row.cells]
            data.append(row_data)
        df = pd.DataFrame(data[1:], columns=data[0])
    elif ext in ['.xls', '.xlsx']:
        df = pd.read_excel(uploaded_file, sheet_name='Sheet1')  # アップロードされたファイルを読み込む

    ax = df.plot(kind='bar')
    image_path = 'app/static/images/graph.png'  # 静的ファイルを保存するパスを指定
    plt.savefig(image_path)
    plt.close()  # 画像を保存した後は閉じます