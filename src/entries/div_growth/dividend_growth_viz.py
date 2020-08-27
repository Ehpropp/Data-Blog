import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()

import src.entries.div_growth.helper_functions as help

def main():
    st.text('first post')
    help.setup_data()

    #st.write(help.DATA['WMT'][2])
    #help.show_stock_graphs('JNJ')
