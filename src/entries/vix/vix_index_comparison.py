import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
pd.plotting.register_matplotlib_converters()

import src.entries.vix.helper_functions as help

def main():
    st.header("How Fear Determines the Market")

    st.write('''
        What if I told you that the stock market movements could be determi
    ''')

    selection = st.sidebar.selectbox('Index', help.INDEXES)