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
        get 10 cents for every share you own. It’s essentially the company paying you for owning a piece of the company (your shares), 
        because that’s what a share is after all.

        One of the benefits of dividends is that you don’t need to sell shares to gain actual income. 
        Some people use this to supplement their income, some use it to reinvest in the same or other stocks, 
        while you keep all the (hopefully) growing shares. The choice is yours.

        Some people don’t see any difference between selling shares and receiving dividends to generate income. 
        There is a point to be made here, but this is a discussion for another post.

        Not all companies pay dividends, and of the ones that do, not all focus on growing the dividends. 
        Companies that do grow their dividends are known as dividend growth stocks. These are the types of stocks 
        Connolly looks for and we’ll use to test the theory.

        Now that we’ve discussed dividends a little, let’s look at DGT. In the words of Connolly himself: 
        “As the dividend rises, so does the [share] price.” That’s the best and shortest explanation I’ve seen. 
        In more detail, DGT states that the annual rate of return of a share price should be approximately the same as 
        the dividend growth rate over time. If that sounds like a mouthful, don’t worry. I have a few examples below.

        Pick any of the companies from the sidebar to view a graph of dividend vs share value from 2000 to 2020.

        Note: All the data collected is from [Yahoo Finance](https://ca.finance.yahoo.com/).
        
        Note: Quick spikes then drops in the graph, like the two in MRU.TO, seem to be errors in the data.
    ''')

    selection = st.sidebar.selectbox('Company', list(help.DATA.keys()))
    help.show_div_graph(selection)

    help.show_share_growth(selection, '2000-01-01')
    help.show_div_growth(selection, '2000-01-01')

    st.write('''
        It should be noted that to normalize the dividend data, I divided corresponding dividend value by stock split ratios.
        This made sense to me since just because the dividend value dropped because of a stock split, doesn't mean they slashed
        the dividends. It just means there are more shares than before, and they couldn't keep the dividend at the same value.

        After looking at the graphs and growth rates, the share growth seems to be quite lower
        than the dividend growth rate for each of the stocks. But let's see what happens to the numbers when we caluclate
        from 2009 to 2020.

        The growth rates below will also change based on the company selection.
    ''')

    help.show_share_growth(selection, '2009-01-01')
    help.show_div_growth(selection, '2009-01-01')

    st.write('''
        Now the both the share and dividend growth rates are much closer (around 2'%' difference between stock and dividend growth), 
        except Metro (MRU.TO), whose dividend growth rate seems to be through the roof.

        So why 2009? Well in 2003 there was a smaller stock market crash because of the dot com bubble, and then in 2008
        there was the major financial crisis which sent us into a recession. So within the first 10 years of the timeframe in the 
        charts, there were two financial crises, one creating a major recession.

        This makes a difference because the companies we're looking at may have had decent cashflow throughout the crises, enabling them
        to keep growing their dividends. But from an investor point of view, people may have been fearful, just not had the money to invest, 
        or had to liquidate investments for a while after. This all could have affected the stock price, while not affecting the dividends as 
        people still need the services these companies provide (like telecomm and consumer staples).

        So it seems that you may need to look at a longer time period than 20 years, especially when the first 10 had two stock market crashes,
        to really see DGT at work. But when you look at 11 years with no recessions, DGT seems to be not so far off. This is just my speculation though. 
        I may lengthen the time period analyzed in the future, but I need to figure out how to fix the errors within the data before I do that.

        If you're interested in reading more about dividend growth from a more experienced investor, you can check out Tom Conolly's website
        [dividendgrowth.ca](http://www.dividendgrowth.ca/dividendgrowth/). He goes quite in depth in his analysis, while still keeping it easy 
        to follow.

        Note: I am looking into making the graphs interactive and allowing readers to look at any stock. It'd be interesting to compare the 
        performance over many years of dividend growth stocks, general dividend paying stocks, and those that don't pay any dividends.
    ''')
