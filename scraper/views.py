from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render, reverse , redirect
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .google_news_scraper import scraper 
import json
from .models import *

# Create your views here.

def home(requests):
    template_name = 'scraper/google_news_scraper.html'
    scraper_details = Google_news.objects.all()
    print(scraper_details)
    
    context={
        'scraper_details' : scraper_details,
        }
    return render(requests,template_name,context)