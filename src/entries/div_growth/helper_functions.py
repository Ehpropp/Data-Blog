'''This will contain the fucntions for the post in this folder'''

import streamlit as st
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()

DATA = {
    'JNJ': [],
    'PG': [],
    'WMT': []
}

@st.cache
def setup_data():
    DATA['JNJ'] = get_files('data/JNJ', '2001-07-01')
    DATA['PG'] = get_files('data/PG', '2004-07-01')
    DATA['WMT'] = get_files('data/WMT', '2000-01-01')

def load_data(path, date, prev_data):
    #print(path)
    data = pd.read_csv(path, index_col='Date', parse_dates=True)
    data = pd.DataFrame(data=data)
    data = data.sort_values(by='Date')
    data = data.loc[date:'2019-12-31', :]

    if 'div' in str(path):
        print(path)
        data = add_div_yield(data, prev_data[1])
    return data

def get_files(path, date):
    data_list = []
    for filename in os.scandir(path):
        data = load_data(filename, date, data_list)
        data_list.append(data)
    return data_list

def add_div_yield(div_data, share_data):
    for date in div_data.index:
        div_data.loc[date, 'Yield'] = (div_data.loc[date, 'Dividends']/share_data.loc[date, 'Close'])*4
    return div_data
    
def show_stock_graphs(name):
    plt.subplots()
    fig = sns.lineplot(x=DATA[name][0].index, y=DATA[name][0]['Close'])
    st.plotly_chart(fig)
