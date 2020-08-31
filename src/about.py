'''File for the about page'''
import streamlit as st

def main():
    st.title('The Data Viz Blog - About')
    st.write('''
        ## Feedback
        I'm Always open to feedback on all of my projects, so if you have any ideas on how to improve the blog, a topic for 
        a post or a post itself, definitely reach out! The best way to reach me would be through LinkedIn, linked in the sidebar
        or at the bottom of this page.

        ## About Me
        This blog was developed and is maintained by Eli Propp. I'm a Computer Engineering student at the University of Waterloo,
        interested in Data Science, Machine Learning, Software Development and Computer Systems. You can learn more about me
        and my expriences from my Website or LinkedIn, linked in the sidebar or down below.

        ## Links
        The GitHub Repo: [ehpropp/Data-Blog](https://github.com/Ehpropp/Data-Blog)  
        LinkedIn: [Eli Propp](https://www.linkedin.com/in/eli-propp-7a13b419a/)  
        My Website: [ehpropp.github.io/Website](https://ehpropp.github.io/Website/)
    ''')
