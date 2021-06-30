'''This will contain the fucntions for the post in this folder'''

import streamlit as st
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()

'''Will store all the pandas dataframes'''
DATA = {
    'BCE.TO': [],
    'JNJ': [],
    'MRU.TO': [],
    'PG': [],
    'WMT': []
}

# @st.cache
def init_data():
    DATA['BCE.TO'] = get_files('data/BCE.TO', '2000-06-01')
    DATA['JNJ'] = get_files('data/JNJ', '2000-01-01')
    DATA['MRU.TO'] = get_files('data/MRU.TO', '2000-01-01')
    DATA['PG'] = get_files('data/PG', '2000-01-01')
    DATA['WMT'] = get_files('data/WMT', '2000-01-01')

    # Not called in the get_files() hierarchy to ensure list indices have been written to
    # Works locally if called in get_files() hierarchy but not on Heroku
    for item in DATA:
        DATA[item][2]['Dividends'] *= 4
        add_div_yield(DATA[item][2], DATA[item][1])
        # Not all stocks have split csv's
        # Prevents Index Error
        if (len(DATA[item]) > 3):
            DATA[item][2] = adj_div_for_split(DATA[item][3], DATA[item][2])

'''
Loads the csv file paths and passes files to load_data().
Returns an array with all the pd df's.
'''
def get_files(path, date):
    data_list = []
    # Ensures os.scandir returns the files in alphabetical order by name
    for filename in sorted(os.scandir(path), key=lambda e: e.name):
        data = load_data(filename, date)
        data_list.append(data)
    return data_list

'''Loads the data, sorts in by date and cuts starting point to date parameter.'''
def load_data(path, date):
    data = pd.read_csv(path, index_col='Date', parse_dates=True)
    data = pd.DataFrame(data=data)
    data = data.sort_values(by='Date')
    data = data.loc[date:'2020-01-01', :]    
    return data

'''
Calculates and adds the dividend yield to the dividend related df.
Dividend yield is not used at the moment.
'''
def add_div_yield(div_data, share_data):
    for date in div_data.index:
        div_data.loc[date, 'Yield'] = (div_data.loc[date, 'Dividends']/share_data.loc[date, 'Close'])
    return div_data

'''
Adjusts the dividends for splits.
Takes all the dividend values before a split date and divides by the split ratio.
Ex: If a dividend was $0.10 before a split, and there was a 2:1 split,
the $0.10 dividend (and all values before the split date) would change to $0.05 (or half the value).
'''
def adj_div_for_split(split_data, div_data):
    for e in split_data.index:
        factor = int(split_data.loc[e, 'Stock Splits'][0])
        div_data.loc[:e, :] /= factor
    return div_data

'''Creates line 2 y-axis line graph of dividend payout and share price  using seaborn.'''
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

'''
Creates line 2 y-axis line graph of dividend yield and share price  using seaborn.
Not used at the moment.
'''
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

'''
Calculates the annual share growth and writes it to the post.
Uses equation: final = initial*(1 + i)^t where t is number of years, i is annual interest rate
'''
def show_share_growth(name, date):
    # Copies dates from index col
    DATA[name][0]['Date'] = DATA[name][0].index
    tmp = DATA[name][0].loc[date:, :]
    # Calculates years based on first and last date in df
    years = (tmp['Date'].iloc[-1] - tmp['Date'].iloc[0]).days/365
    # Calculates exponent base as (last share price)/(first share price)
    base = tmp['Close'].iloc[-1]/tmp['Close'].iloc[0]
    growth = round((base**(1/years) - 1)*100, 2)
    st.write('Annual Share Growth: ' + str(growth) + "%")

'''
Calculates the annual dividend growth and writes it to the post.
Uses equation: final = initial*(1 + i)^t where t is number of years, i is annual interest rate
'''
def show_div_growth(name, date):
    # Copies dates from index col
    DATA[name][2]['Date'] = DATA[name][2].index
    tmp = DATA[name][2].loc[date:, :]
    # Calculates years based on first and last date in df
    years = (tmp['Date'].iloc[-1] - tmp['Date'].iloc[0]).days/365
    # Calculates exponent base as (last dividend)/(first dividend)
    base = tmp['Dividends'].iloc[-1]/tmp['Dividends'].iloc[0]
    growth = round((base**(1/years) - 1)*100, 2)
    st.write('Annual Dividend Growth: ' + str(growth) + "%")
