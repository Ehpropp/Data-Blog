'''File for the posts page'''
import src.entries.post_list
import importlib
import streamlit as st

'''
Imports all the main files containing the posts.
The relative file paths are stored in the POSTS dict
in post_list.py.
'''
@st.cache
def import_posts():
    for file in src.entries.post_list.POSTS.values():
        if file == "home":
            continue
        globals()[file] = importlib.import_module(file)


'''Since it only needs to import everything once, it's called right when the app starts'''
import_posts()

def main():
    selection = st.sidebar.selectbox("", list(src.entries.post_list.POSTS.keys()))
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

        Posts will be previewed here as they are uploaded to the blog.
        """
    )
