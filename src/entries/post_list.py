'''File to store the posts'''

'''
This will store the dictionary that stores the post names and related file.
'Overview' will be the main page that the user goes to when selecting the 'posts' page.
It is currently just a string as it does not have it's own file.
If changing the dictionary value for 'Overview', change the if statement in posts.py.
'''
POSTS = {
    'Overview': 'home',
    'Dividend Growth Visualization': 'src.entries.div_growth.dividend_growth_viz'
}
