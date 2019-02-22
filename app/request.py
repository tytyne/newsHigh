from app import app
import urllib.request
import json
from .models import new
from .models import source
New = new.New
Source=source.Source
# Getting api key
api_key = app.config["NEW_API_KEY"]

# Getting the new base url
base_url = app.config["NEW_API_BASE_URL"]
print(base_url)
SOURCE_url = app.config["SOURCE_API_BASE_URL"]
print(SOURCE_url)

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''


    get_sources_url = SOURCE_url.format(api_key)
  
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        print(get_sources_data)
        get_sources_response = json.loads(get_sources_data)
        print(get_sources_response)
        source_articles = None

        if get_sources_response['sources']:
            source_articles_list = get_sources_response['sources']
            source_articles = process_source(source_articles_list)
    
    return source_articles

def process_source(source_list):
    source_articles = []

    for  source_item in  source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description =  source_item.get('description')


        if source:
            source_object = Source(id,name,description)
            source_articles.append(source_object)

    return source_articles


def get_news(name):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = 'https://newsapi.org/v2/everything?sources={}&apiKey=30752d2a0e6b418ba7a08cf4eab5686e'.format(name)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        print(get_news_response)
        new_articles = None

        if get_news_response['articles']:
            new_articles_list = get_news_response['articles']
            new_articles = process_articles(new_articles_list)

    return new_articles


def process_articles( new_list):
    '''
    Function  that processes the new result and transform them to a list of Objects

    Args:
        new_list: A list of dictionaries that contain  new details

    Returns :
        new_articles: A list of  new objects
    '''
    new_articles = []
    for  new_item in  new_list:
        id = new_item.get('id')
        title =  new_item.get('title')
        author=  new_item.get('author')
        url=new_item.get('url')
        urlToImage = new_item.get('urlToImage')
        description =  new_item.get('description')
        publishedAt =  new_item.get('publishedAt')
        content =  new_item.get('content')

        if urlToImage:
            new_object = New(id,title, author,url,urlToImage, description,  publishedAt,content)
            new_articles.append( new_object)

    return new_articles



