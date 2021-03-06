from  .models import Sources, Articles
from datetime import datetime
import json
import urllib.request
import os

# getting the api key
api_key = None

# getting the news base url
base_url = None

# getting the articles url
articles_url = None

# function to configure request to the api key


def configure_request(app):
    global api_key, base_url, articles_url
    api_key = os.environ.get('NEWS_API_KEY')
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']

# function to get sources of the news


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format('sources',api_key, category)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            sources_results_list =  get_sources_response['sources']
            source_results = process_sources(sources_results_list)

    return source_results  


def process_sources(sources_list):
    """
    function that processs the news sourecs results and turn them into list of objects
    Args:
        source_list: list of dictionaries that contain sources details
    Returns:
        sources results,a list of sources objects
    """
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        sources_object = Sources(
            id, name, description, url, category, language, country)
        sources_results.append(sources_object)
    return sources_results


def get_articles(id):
    """
    Function that processes the articles and return a list of articles objects
    """
    get_articles_url = articles_url.format(id, api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())
        articles_object = None
        if articles_object['articles']:
            articles_object = process_articles(articles_results['articles'])
    return articles_object


def process_articles(articles_list):
    """
    function to process the list of articles
    """
    articles_object = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')

        if image:
            articles_result = Articles(id,author,title,description,url,image,date)
            articles_object.append(articles_result)



    return articles_object