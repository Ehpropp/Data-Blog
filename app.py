"""Main module for the blog"""
import streamlit as st

import src.home
import src.posts
import src.about

MAIN_PAGES = {
    "Home": src.home,
    "Posts": src.posts,
    "About": src.about,
}


def main():
    """Main function for the app"""

    st.sidebar.title('Data Viz Blog')
    st.sidebar.header('Pages')
    selection = st.sidebar.radio('Go to', list(MAIN_PAGES.keys()))

    # Every page has a main function which executes necessary code for that page
    page = MAIN_PAGES[selection]
    page.main()

    st.sidebar.header('About')
    st.sidebar.info(
        "This blog is maintained by Eli Propp. "
        "You can learn more about me on the about page or at "
        "[ehpropp.github.io/Website](https://ehpropp.github.io/Website/)"
    )

    st.sidebar.header('Links')
    st.sidebar.info(
        "LinkedIn: [Eli Propp](https://www.linkedin.com/in/eli-propp-7a13b419a/)  \n"
        "GitHub: [Eli Propp](https://github.com/Ehpropp)"
    )

if __name__ == '__main__':
    main()
