from .request import get_news
from flask import render_template
from app import app
from .request import get_news, get_sources
# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular new
    popular_sources= get_sources('popular')
    # print(popular_sources)
    # general_sources= get_sources('general')
    # entertainement_sources= get_sources('entertainement')
    title = 'Home - Welcome to The best new Review Website Online'
    return render_template('index.html', title=title, popular=popular_sources)



@app.route('/source/<id>')
def new(id):
    '''
    View new page function that returns the new details page and its data
    '''
    article = get_news(id)
    title ='hell'

    return render_template('new.html', title=title, article=article)
