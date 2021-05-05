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
    help.init()

    st.header("How Fear Determines the Market")

    st.write('''
        Some text
    ''')

    selection = st.sidebar.selectbox('Index', help.INDEXES)
    help.make_line_chart(selection)
    help.make_scatter_plot(selection)
    help.show_pd_corr()

    st.write('''
        Disclaimer: None of the information provided here is investment advice. It is purely for entertainment purposes. 
        Before making any investment, it solely your responsibility to do research and understand what you're investing in.
    ''')