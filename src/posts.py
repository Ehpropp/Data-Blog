import src.entries.post_list
import streamlit as st


def main():
    st.title('Data Blog')

    st.write('''
        This is the main page for the posts. You can select a post
        from the dropdown menu in the sidebar.

        Posts will be previewed here as they are uploaded to the blog.
    ''')

    selection = st.sidebar.selectbox(
        '', list(src.entries.post_list.POSTS.keys()))
    page = src.entries.post_list.POSTS[selection]
    page.main()
