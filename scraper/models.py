from django.db import models

# Create your models here.
class Google_news(models.Model):
    
    description = models.TextField()
    details = models.CharField(max_length=40)
    date_time = models.DateTimeField()
    image_url = models.URLField()
