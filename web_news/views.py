from django.shortcuts import render
import json
import requests
from requests import api

#newsapi key: https://newsapi.org/v2/top-headlines?country=it&sortBy=popularity&apiKey=09a5781760394a0ebc73e4e0276c603c


def homeview(request):
    news_api_request = requests.get('https://newsapi.org/v2/top-headlines?country=it&apiKey=09a5781760394a0ebc73e4e0276c603c')
    api1 = json.loads(news_api_request.content)
    return render(request, 'web_news/homepage.html', {'api':api1})