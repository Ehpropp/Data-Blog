'''This will contain the fucntions for the post in this folder'''

import streamlit as st
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()

DATA = {
    'BCE.TO': [],
    'JNJ': [],
    'MRU.TO': [],
    'PG': [],
    'WMT': []
}

@st.cache
def init_data():
    DATA['BCE.TO'] = get_files('data/BCE.TO', '2000-06-01')
    DATA['JNJ'] = get_files('data/JNJ', '2000-01-01')
    DATA['MRU.TO'] = get_files('data/MRU.TO', '2000-01-01')
    DATA['PG'] = get_files('data/PG', '2000-01-01')
    DATA['WMT'] = get_files('data/WMT', '2000-01-01')

    for items in DATA.values():
        items[2]['Dividends'] *= 4
        add_div_yield(items[2], items[1])
        if (len(items) > 3):
            items[2] = adj_div_for_split(items[3], items[2])

def get_files(path, date):
    data_list = []
    for filename in os.scandir(path):
        data = load_data(filename, date, data_list)
        data_list.append(data)
    return data_list

def load_data(path, date, prev_data):
    data = pd.read_csv(path, index_col='Date', parse_dates=True)
    data = pd.DataFrame(data=data)
    data = data.sort_values(by='Date')
    data = data.loc[date:'2020-01-01', :]    
    return data

def add_div_yield(div_data, share_data):
    for date in div_data.index:
        div_data.loc[date, 'Yield'] = (div_data.loc[date, 'Dividends']/share_data.loc[date, 'Close'])
    return div_data

def adj_div_for_split(split_data, div_data):
    for e in split_data.index:
        factor = int(split_data.loc[e, 'Stock Splits'][0])
        div_data.loc[:e, :] /= factor
    return div_data
    
def show_div_graph(name):
    fig, ax1 = plt.subplots(figsize=(8,4))
    ax1.set_title(name + ' Share Price vs Annual Dividend', fontsize=14)
    ax1 = sns.lineplot(x=DATA[name][0].index, y=DATA[name][0]['Close'], color='blue')
    ax1.set_xlabel('Date', fontsize=12)
    ax1.set_ylabel('Share Price', fontsize=12, color='blue')
    ax2 = ax1.twinx()
    ax2 = sns.lineplot(x=DATA[name][2].index, y=DATA[name][2]['Dividends'], color='orange')
    ax2.set_ylabel('Annual Dividend Payout', fontsize=12, color='orange')
    st.pyplot(fig)

def show_yield_graph(name):
    fig, ax1 = plt.subplots(figsize=(8,4))
    ax1.set_title(name + ' Share Price vs Annual Dividend Yield', fontsize=14)
    ax1 = sns.lineplot(x=DATA[name][0].index, y=DATA[name][0]['Close'], color='blue')
    ax1.set_xlabel('Date', fontsize=12)
    ax1.set_ylabel('Share Price', fontsize=12, color='blue')
    ax2 = ax1.twinx()
    ax2 = sns.lineplot(x=DATA[name][2].index, y=DATA[name][2]['Yield'], color='orange')
    ax2.set_ylabel('Annual Dividend Yield', fontsize=12, color='orange')
    st.pyplot(fig)

def show_share_growth(name, date):
    DATA[name][0]['Date'] = DATA[name][0].index
    tmp = DATA[name][0].loc[date:, :]
    years = (tmp['Date'].iloc[-1] - tmp['Date'].iloc[0]).days/365
    base = tmp['Close'].iloc[-1]/tmp['Close'].iloc[0]
    growth = round((base**(1/years) - 1)*100, 2)
    st.write('Annual Share Growth: ' + str(growth) + "%")

def show_div_growth(name, date):
    DATA[name][2]['Date'] = DATA[name][2].index
    tmp = DATA[name][2].loc[date:, :]
    years = (tmp['Date'].iloc[-1] - tmp['Date'].iloc[0]).days/365
    base = tmp['Dividends'].iloc[-1]/tmp['Dividends'].iloc[0]
    growth = round((base**(1/years) - 1)*100, 2)
    st.write('Annual Dividend Growth: ' + str(growth) + "%")
