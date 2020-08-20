import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()


main_menu = st.sidebar

main_menu.title('Data Blog')
main_menu.header('Main Menu')

slc_box = main_menu.selectbox(
    'Pages',
    ('Home', 'Posts')
)

main_menu.subheader('Profiles & Contact')
main_menu.markdown('''

LinkedIn: [Eli Propp](https://www.linkedin.com/in/eli-propp-7a13b419a/)  
Github: [Eli Propp](https://github.com/Ehpropp)  
[My Website](https://ehpropp.github.io/Website/)

''')


if slc_box == 'Home':
    st.title('The Data Blog')

    st.markdown('''

    Welcome to my data science blog!
    My name is Eli Propp. I'm a Computer Engineering Student
    at the University of Waterloo, interested in 
    data science, deep learning, software and finance.

    The blog posts will be on a range of topics,
    but I'll be starting with finance. It'll be 
    oriented in a way that you can understand 
    the entire topic with sources in the post,
    at least at a high level.

    Select the post page from the dropdown menu in the sidebar
    to start looking at my posts.

    Let me know if you have any tips or ideas for posts
    or the general website. I'm open to an ideas on how
    I can make this better. 

    You can contact me from any of the links in the sidebar. 

    ''')
