import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generate_base64_graph(type, path):
    # 仮のデータを生成（ここでは単純なバーチャートを例にします）
    df = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [4, 7, 1, 8]
    })

    # グラフを描画
    plt.figure()
    df.plot(kind='bar', x='Category', y='Values')
    plt.tight_layout()

    # 画像をBase64エンコーディングして返す
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    base64_string = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    return base64_string