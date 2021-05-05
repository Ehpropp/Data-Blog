'''File for the about page'''
import streamlit as st

def main():
    st.title('The Data Viz Blog - About')
    st.write('''
        ## Feedback
        I'm Always open to feedback on all of my projects, so if you have any ideas on how to improve the blog, a topic for 
        a post or a post itself, definitely reach out! The best way to reach me is through LinkedIn or my Website, linked in the sidebar
        and down below.

        Also if you have an idea, suggestion or post, and have worked on it yourself, fork the repo and make a pull request! I'd love to 
        see ideas anyone has to add to the blog. All I ask is for commented code, and if you're writing a post, make sure all necessary
        functions are executed in a main() function in your python file.

        ## About Me
        This blog was developed and is maintained by me, Eli Propp. I'm a Computer Engineering student at the University of Waterloo,
        interested in Data Science, Machine Learning, Software Development and Computer Systems. You can learn more about me
        and my expriences from my Website or LinkedIn, linked in the sidebar and down below.

        ## Resources
        Definitely check out the Streamlit website, and an open-source application called awesome-streamlit, developed and maintained 
        by Mark Skov Madsen. You can access them in the links down below.

        ## Links
        The GitHub Repo: [elipropp/Data-Blog](https://github.com/elipropp/Data-Blog)  
        LinkedIn: [Eli Propp](https://www.linkedin.com/in/elipropp)  
        My Website: [elipropp.github.io/Website](https://elipropp.github.io/Website/)

        Streamlit: [streamlit.io](https://www.streamlit.io/)  
        Awesome-Streamlit: [awesome-streamlit.org](http://www.awesome-streamlit.org)  
        Awesome-Streamlit Repo: [MarkSkovMadsen/awesome-streamlit](https://github.com/MarcSkovMadsen/awesome-streamlit)

    ''')
