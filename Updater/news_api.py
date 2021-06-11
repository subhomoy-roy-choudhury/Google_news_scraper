import os
import requests
from scraper.models import Google_news
from bs4 import BeautifulSoup
#from scheduler.config_stuff import config


def scraper():
    try :

        r = requests.get("https://news.google.com/search?q=nri&hl=en-IN&gl=IN&ceid=IN%3Aen")
        print(r.status_code)  
        content = r.text
        soup = BeautifulSoup(content, "html.parser")

        st_divs1 = soup.find_all('div',{"class" : "NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc"})
        print(len(st_divs1))

        data = []

        for i in range(len(st_divs1)) :
            # print('*'*40)
            st_divs = soup.find_all('div',{"class" : "NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc"})[i]
            detail = st_divs.find('h3',{"class" : "ipQwMb ekueJc RD0gLb"}).text
            description = st_divs.find('span',{"class" : "xBbh9"}).text
            date_time = st_divs.find('time',{"class" : "WW6dff uQIVzc Sksgp"})['datetime']
            image = 'https://moonvillageassociation.org/wp-content/uploads/2018/06/default-profile-picture1.jpg'
            try:
                image_url = st_divs.find('img',{"class" : "tvs3Id QwxBBf"})['src']
            except Exception as e:
                print(e)
                pass

            # print(detail,description,date_time,image_url)
            # print('*'*40)

            scraper_data = {}
            scraper_data['details'] = detail
            scraper_data['description'] = description
            scraper_data['date_time'] = date_time
            scraper_data['image_url'] = image_url

            data.append(scraper_data)

    # print(data)
        return data
    except :

        return None



def _get_forecast_json():
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    encoded_city_name = 'Los%20Angeles'
    country_code = 'us'
    access_token = os.environ.get('OPENWEATHERMAPS_TOKEN')
  
    r = requests.get('{0}?q={1},{2}&APPID={3}'.format(
        base_url, 
        encoded_city_name, 
        country_code, 
        access_token))
        
    try:
        r.raise_for_status()
        return r.json()
    except:
        return None

def update_googlenews():

    json = scraper()
    # print(json)
    if json is not None:
        try:
            for i in json:
                scrape = Google_news.objects.get_or_create(description=i['description'],details=i['details'],date_time=i['date_time'],image_url=i['image_url'])
                print(i['details'],scrape)
                scrape1 = Google_news.objects.filter(description=i['description'],details=i['details'],image_url=i['image_url'])
                if len(scrape1) > 1 :
                    print(scrape1)
                print("saving...\n" + scrape)
        except:
            pass