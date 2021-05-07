import streamlit as st
import os
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
pd.plotting.register_matplotlib_converters()

INDEXES = ['S&P 500', 'NASDAQ', 'DOW JONES']

DATA = {
    'VIX': pd.DataFrame(),
    'S&P 500': pd.DataFrame(),
    'NASDAQ': pd.DataFrame(),
    'DOW JONES': pd.DataFrame(),
    'PERCENT CHANGE': pd.DataFrame()
}

def init():
    get_data()
    modify_data()
    create_percent_change()

def get_data():
    DATA['VIX'] = pd.DataFrame(yf.Ticker("^vix").history(period="max", interval="1d", start="2000-01-01", end="2020-12-30"))
    DATA['S&P 500'] = pd.DataFrame(yf.Ticker("^GSPC").history(period="max", interval="1d", start="2000-01-01", end="2020-12-30"))
    DATA['NASDAQ'] = pd.DataFrame(yf.Ticker("^IXIC").history(period="max", interval="1d", start="2000-01-01", end="2020-12-30"))
    DATA['DOW JONES'] = pd.DataFrame(yf.Ticker("^DJI").history(period="max", interval="1d", start="2000-01-01", end="2020-12-30"))

def modify_data():
    DATA['VIX']['Percent_Change'] = DATA['VIX'].apply(lambda row: (row.Close - row.Open)/row.Close * 100, axis=1)
    DATA['S&P 500']['Percent_Change'] = DATA['S&P 500'].apply(lambda row: (row.Close - row.Open)/row.Close * 100, axis=1)
    DATA['NASDAQ']['Percent_Change'] = DATA['NASDAQ'].apply(lambda row: (row.Close - row.Open)/row.Close * 100, axis=1)
    DATA['DOW JONES']['Percent_Change'] = DATA['DOW JONES'].apply(lambda row: (row.Close - row.Open)/row.Close * 100, axis=1)

def create_percent_change():
    DATA['PERCENT CHANGE']['VIX'] = DATA['VIX']['Percent_Change']
    DATA['PERCENT CHANGE']['S&P 500'] = DATA['S&P 500']['Percent_Change']
    DATA['PERCENT CHANGE']['NASDAQ'] = DATA['NASDAQ']['Percent_Change']
    DATA['PERCENT CHANGE']['DOW JONES'] = DATA['DOW JONES']['Percent_Change']

def make_line_chart(index_name):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=DATA['VIX'].index, y=DATA['VIX']['Close'], name="VIX"),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(x=DATA[index_name].index, y=DATA[index_name]['Close'], name=index_name),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(title_text="CBOE VIX vs. " + index_name + " Line Chart")

    # Set x-axis title
    fig.update_xaxes(title_text="Date")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b></b> VIX Value", secondary_y=False)
    fig.update_yaxes(title_text=index_name + " Value", secondary_y=True)

    st.plotly_chart(fig)

def make_scatter_plot(index_name):
    fig = px.scatter(DATA['PERCENT CHANGE'], x='VIX', y=index_name, trendline="ols")
    fig.update_layout(title_text="CBOE VIX vs. " + index_name + " Scatter Plot")
    fig.update_xaxes(title_text="VIX Daily Percent Change")
    fig.update_yaxes(title_text=index_name + " Daily Percent Change")
    st.plotly_chart(fig)

def show_pd_corr():
    st.write(DATA['PERCENT CHANGE'].corr())