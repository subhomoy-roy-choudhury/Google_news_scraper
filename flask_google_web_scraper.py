
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request, jsonify
import os
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def scraper():
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



@app.route('/',methods=['GET'])
def hello_world():
    scraper1 = scraper()
    # return 'Hello from Flask!'
    return jsonify(scraper1)


if __name__ == '__main__':
    app.run()