from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from Updater import news_api

        
def start():
        scheduler = BackgroundScheduler()
        scheduler.add_job(news_api.update_googlenews, 'interval', minutes=5)
        scheduler.start()