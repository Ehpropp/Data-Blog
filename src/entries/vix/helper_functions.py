import streamlit as st
import os
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()

INDEXES = ['S&P 500', 'NASADAQ', 'DOW JONES']

DATA = {
    'VIX': '',
    'S&P 500': '',
    'NASDAQ': '',
    'DOW JONES': '',
    'PERCENT CHANGE': ''
}

def init():
    DATA['VIX'] = pd.DataFrame(yf.Ticker("^vix").history(period="max", interval="1d", start="2000-01-01", end="2020-12-30"))
    DATA['S&P 500'] = pd.DataFrame(yf.Ticker("^GSPC").history(period="max", interval="1d", start="2000-01-01", end="2020-12-30"))
    DATA['NASDAQ'] = pd.DataFrame(yf.Ticker("^IXIC").history(period="max", interval="1d", start="2000-01-01", end="2020-12-30"))
    DATA['DOW JONES'] = pd.DataFrame(yf.Ticker("^DJI").history(period="max", interval="1d", start="2000-01-01", end="2020-12-30"))