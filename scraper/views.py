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
    try :
        scraper1 = scraper()
        # print(scraper1)
        with open('scraper/google_news_scraper.json','w') as file :
            json.dump(scraper1,file,ensure_ascii=False, indent=1)
        
        for i in scraper1:
            scrape = Google_news.objects.get_or_create(description=i['description'],details=i['details'],date_time=i['date_time'],image_url=i['image_url'])
            scrape1 = Google_news.objects.filter(description=i['description'],details=i['details'],image_url=i['image_url'])
            if len(scrape1) > 1 :
                print(scrape1)

        scraper_details = Google_news.objects.all()
        print(scraper_details)

    except Exception as e:
        print(e)
        pass

    context={
        'scraper_details' : scraper_details,
        }
    return render(requests,template_name,context)