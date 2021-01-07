from django.db import models

class Registration(models.Model):
        name = models.CharField(max_length=50)
        email = models.EmailField()
        contact = models.BigIntegerField(max_length=13)
        speciality = models.CharField(max_length=20)
        password = models.CharField(max_length=20)

class About(models.Model):
        description = models.TextField('Description')
        image = models.ImageField(upload_to='images/about/')

class Service(models.Model):
        service_name = models.CharField(max_length=50)
        description = models.TextField('description')
        image = models.ImageField(upload_to='images/services/')

class Reviews(models.Model):
        firstname = models.CharField(max_length=25)
        lastname = models.CharField(max_length=25)
        review = models.TextField('review')

class Team(models.Model):
        name =  models.CharField(max_length=50)
        speciality = models.CharField(max_length=100)
        description = models.TextField('description')

class Makeup(models.Model):
        service = models.CharField(max_length=50)
        description = models.TextField('description')

class LatestNews(models.Model):
        news_header = models.CharField(max_length=100)
        news_description = models.TextField('news_description')
        image = models.ImageField(upload_to='images/news/')
        date = models.DateField(max_length=12)

class Brands(models.Model):
        name = models.CharField(max_length=50)
        image = models.ImageField(upload_to='images/brand/')

class Blog(models.Model):
        title = models.CharField(max_length=50)
        description = models.TextField('description')
        image = models.ImageField(upload_to='images/blog')
        date = models.DateField(max_length=12)


