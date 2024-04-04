import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from .graph_method import bar,line,hist,box,area,pie,scatter

def graph(uploaded_file):
    filename = uploaded_file.filename
    _, ext = os.path.splitext(filename)
    
    if ext in ['.xls', '.xlsx']:
        df = pd.read_excel(uploaded_file)  # アップロードされたファイルを読み込む

    bar(df)
    line(df)
    hist(df)
    box(df)
    area(df)
    pie(df)
    scatter(df)
