# Generated by Django 3.2 on 2021-06-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='google_news',
            name='details',
            field=models.CharField(max_length=100),
        ),
    ]
