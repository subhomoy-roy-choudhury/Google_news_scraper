from django.db import models

# Create your models here.
class Google_news(models.Model):
    
    description = models.TextField()
    details = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    image_url = models.URLField(max_length=200)
