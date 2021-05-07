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
        What's the S&P 500 value going to be tomorrow? How about next week? Many people might tell you they know (if they
        do, don't listen to them), but frankly no one does. In the long term, the stock market tends to go up. It's been 
        doing so for over a century, and will probably continue to do so (assuming the countries stay stable). 
        But what about in the short term?

        Many people have the goal to predict the stock market's value tomorrow, next week or even next month, and 
        it's easy to see why. If someone is accurately able to do so, they'd be be rich in no time. But as nice 
        of a thought as that is, it's near impossible. There are just too many factors that go into it, not all of which are quantifiable. 
        
        But what if I told you that you could quantify a seemingly unquantifiable factor, like investor fear? After all, 
        when people are fearful, they tend to sell assets (stocks, ETFs, Mutual Funds etc.) to cut their (most likely temporary) losses. 
        And when they do, they're willing to sell at a slightly lower price, which causes values to go down (in the short term that is). 
        It makes sense logically, but does fear actually rule the market? And how do you quantify fear anyways?

        To tackle the second question first, we can look to the Chicago Board Options Exchange Volatility Index, known as the VIX.
        This index is a derivative of people speculating on S&P 500 options, meaning they're placing bets on whether the S&P 500 index 
        will go up or down over the next month. Now what does this have to with fear? Well, another name for the VIX is the 'fear index' 
        (I even googled 'fear index/gauge' and the 'VIX' is at the top), because when people are fearful and think the S&P 500 is going to
        go down, the VIX generally rises (higher volatility), and when they think the market will go up, the VIX generally goes down
        (lower volatility). There's a decent amount of complex math that goes into calcualting the VIX, but if you're interested you can
        read more about it here: [VIX calculation](https://www.investopedia.com/articles/active-trading/070213/tracking-volatility-how-vix-calculated.asp).

        So let's say we use the VIX as out metric for qunatifying short term fear. Does it determine the market?

        While it may not predict the market, it does seems to be pretty proportional. Let's take a look at the VIX versus some of the
        major U.S. indexes, the S&P 500, NASDAQ and DOW JONES. Select one of the indexes in the dropdown menu on the left and take a look
        at the line chart below. It's interactive, so play around with it, and if you want to make it bigger, just expand it in the top
        right of the chart.
    ''')

    selection = st.sidebar.selectbox('Index', help.INDEXES)
    st.plotly_chart(help.make_line_chart(selection))

    st.write(''' 
        After looking at the line chart for each index, it seems that maybe the VIX and the index values could be negatively correlated. 
        Looking at the major market crashes, like in 2009 and just this past year in 2020, we can see the VIX sky rocketed around the same
        time as the crash. Now it looks like the NASDAQ didn't drop as much as the S&P 500 or DOW JONES, but that could be because it's
        mostly comprised of the technology sector, whereas the S&P 500 and DOW have a broader mix of stocks from many sectors.

        Not only during the major crashes, but at a glance it seems like there's a bit of negative correlation throughtout the data, 
        with some spikes in the VIX happening when there's a drop in the markets.

        To get a better idea if fear heavily influences the market, let's compare the daily percent change of the VIX to that of the markets,
        and see if there's a trend. Take a look at the scatter plot below (it's also interactive). 
    ''')

    st.plotly_chart(help.make_scatter_plot(selection))

    st.write('''
        Now the relationship is starting to look much clearer. Even without the trendline, it's pretty clear that each of the indexes 
        have some negative correlation with the VIX. The points cluster around the origin since most of the time the market doesn't make 
        huge jumps. But the trend is clear: more often than not, when the VIX goes up, the market goes down, and vice versa.

        What's even more interesting is some of the information the trendline gives us.

        If you hover over the trendline, you can see the equation and R^2 value calculated by plotly (the library that made the graphs). 
        All it did was linear regression, and if that;s unfamiliar to you, it simply tries to find the equation of a line that minimizes 
        the error to predict the data points.

        The R^2 value is known as the 'coefficient of determination' in statistics, and can be used to determine how well the line fits 
        the data points. In short, the lower the R^2 value, the less accurate the line is at predicting the data points, with an R^2 of 
        1 being a perfect fit, and 0 being the same accuracy as a horizontal line.

        Comparing the R^2 values, the S&P 500's is around 0.39, NASDAQ around 0.35, and DOW JONES around 0.345. It makes sense that the 
        S&P 500's is slightly better, since the VIX is a direct derivative from the S&P 500, not the other indexes.

        It may seem that these R^2 values aren't so great, and for general regression cases they aren't. But another way to look at 
        R^2 is the amount of variability accounted for. So the S&P 500 having an R^2 of 0.39 shows around 39 percent of the variability 
        of the daily percent change is correlated with the daily percent change of the VIX. Now for something as complex as the stock market, 
        with things from company earnings to politics to investor sentiment playing a role in its price, a 39 percent correlation with 
        one number seems pretty high. 

        And yes, there's a lot that goes into calculating the VIX value, but at the end of the day it just tries to quantify people's 
        expectations of the market (S&P 500 specifically) in the short term, also known as investor fear. 

        Now you may not be able to use the VIX to predict the short term stock market movements (nor should you in my opinion), but an 
        increase or decrease in its value can give some insight into investor sentiment on the short term performance/stability/volatility 
        of the market.

        As I mentioned at the beginning, the market generally to rises over long time periods (I'm talking decades), so from this perspective 
        investor sentiment/fear, which is usually emotional and not based on a long term point of view, doesn't matter much. But looking 
        at the short term, especially within one day, it seems like fear might just determine the market.
    ''')

    st.write('''
        Disclaimer: None of the information provided here is investment advice. It is purely for entertainment purposes. 
        Before making any investment, it solely your responsibility to do research and understand what you're investing in.
    ''')