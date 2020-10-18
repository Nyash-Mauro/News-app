from .models import Sources, Articles
from datetime import datetime
import os
import json
import urllib.request

# getting the api key
api_key = None

# getting the news base url
base_url = None

# getting the articles url
articles_url = None

# function to configure request to the api key


def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']
