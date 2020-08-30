import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()

import src.entries.div_growth.helper_functions as help

def main():
    help.init_data()

    st.header('The Dividend Growth Theory')

    st.write('''
        As per the title of the post, I'll be discussing and visualizing the dividend growth theory (DGT). 
        This theory is one that Tom Connolly, a household name in Canada when it comes to dividend investing, is a huge proponent of. 
        But before we get into the theory, we should discuss dividends themselves quickly.

        Dividends are a piece of a company’s earnings that the company pays out to the shareholders. That’s it. 
        Usually payed quarterly, the board of directors will declare a dividend at some point, and when the set date comes, 
        you get the value of the dividend for every share of the company you own. So if the dividend is $0.10, that means you'll
        get 10 cents for every share you own. It’s essentially the company paying you for owning a piece of the company, 
        because that’s what a share is after all.

        One of the benefits of dividends is that you don’t need to sell shares to gain actual income. 
        Some people use this to supplement their income, some use it to reinvest in the same or other stocks, 
        while you keep all the (hopefully) growing shares. The choice is yours.

        Some people don’t see any difference between selling shares and receiving dividends. 
        There is a point to be made here, but this is a discussion for another post.

        Not all companies pay dividends, and of the ones that do, not all focus on growing the dividends. 
        Companies that do grow their dividends are known as Dividend Growth Stocks (DGS). These are the types of stocks 
        Connolly looks for and we’ll use to test the theory.

        Now that we’ve discussed dividends a little, let’s look at DGT. In the words of Connolly himself: 
        “As the dividend rises, so does the [share] price.” That’s the best and shortest explanation I’ve seen. 
        In more detail, DGT states that the annual rate of return of a share price should be approximately the same as 
        the dividend growth rate over time. If that sounds like a mouthful, don’t worry. I have a few examples below.

        Pick any of the companies from the sidebar to view a graph of dividend vs share value from 2000 to 2020.

        Note: All the data collected is from Yahoo Finance.
        
        Note: Quick spikes then drops in the graph, like the two in MRU.TO, seem to be errors in the data.
    ''')

    selection = st.sidebar.selectbox('Company', list(help.DATA.keys()))
    #help.show_div_graph(selection)

    help.show_share_growth(selection, '2000-01-01')
    help.show_div_growth(selection, '2000-01-01')

    st.write('''
        It should be noted that to normalize the dividend data, I divided corresponding dividend value by stock split ratios.
        This made sense to me since just because the dividend value dropped because of the stock split, doesn't mean they slashed
        the dividends. It just means there are more shares than before, and they couldn't keep the dividend at the same value.

        After looking at the graphs and growth rates, the share growth seems to be quite lower
        than the dividend growth rate for each of the stocks. But let's see what happens to the numbers when we caluclate
        from 2009 to 2020.

        The growth rates will change based on the company selection.
    ''')

    help.show_share_growth(selection, '2009-01-01')
    help.show_div_growth(selection, '2009-01-01')
