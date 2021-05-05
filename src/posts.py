'''File for the posts page'''
import src.entries.post_list
import importlib
import streamlit as st

'''
Imports all the main files containing the posts.
The relative file paths are stored in the POSTS dict
in post_list.py.
'''

def import_posts():
    for file in src.entries.post_list.POSTS.values():
        if file == "home":
            continue
        globals()[file] = importlib.import_module(file)
    
    for file in src.entries.post_list.POST_HELPERS.values():
        if file == 'none':
            continue
        globals()[file] = importlib.import_module(file)


'''Since it only needs to import everything once, it's called right when the app starts'''
import_posts()

def main():
    st.title('The Data Viz Blog - Posts')
    selection = st.sidebar.selectbox('Posts', list(src.entries.post_list.POSTS.keys()))
    page = src.entries.post_list.POSTS[selection]

    if page == "home":
        write_main_page()
    else:
        # Turns the page from a string to the file path object
        eval(page).main()

'''Displays the text for the Overview page'''
def write_main_page():
    st.write(
        """
        This is the main page for the posts. You can select a post
        from the dropdown menu in the sidebar.

        Recent posts will be previewed here as they are uploaded to the blog.
        """
    )

    # Post #1 Info
    st.info(
        '''
        ### How Fear Determines the Market - Post #2
        In this post I'll be taking a look at the volatility index (VIX) and seeing how its
        movements are related to the stock market.

        Go to the sidebar and select VIX vs. Index.
        '''
    )

    # Post #1 Info
    st.info(
        '''
        ### Dividend Growth Visualization - Post #1
        In this post I'll be discussing, visualizing, and analysing the Dividend Growth Theory,
        looking at if and how dividends can influence a stock price.

        Go to the sidebar and select 'Dividend Growth Visualization' from the dropdown menu.
        '''
    )
