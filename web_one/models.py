from os import name
from django.db import models

# Create your models here.

class HomeModel(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    price = models.CharField(max_length=50)
    link = models.URLField()

    
    def __str__(self):
        return self.title
    
    

class TrendModel(models.Model):
    ttitle = models.CharField(max_length=120)
    timage = models.ImageField()
    tprice = models.CharField(max_length=50)
    tlink = models.URLField()
    
    def __str__(self):
        return self.ttitle


class RelatedModel(models.Model):
    rtitle = models.CharField(max_length=120)
    rimage = models.ImageField()
    rprice = models.CharField(max_length=50)
    rlink = models.URLField()
    
    def __str__(self):
        return self.rtitle


class Accessories(models.Model):
    atitle = models.CharField(max_length=120)
    aimage = models.ImageField()
    aprice = models.CharField(max_length=50)
    alink = models.URLField()
    
    def __str__(self):
        return self.atitle
    
class Nintendo(models.Model):
    ntitle = models.CharField(max_length=120)
    nimage = models.ImageField()
    nprice = models.CharField(max_length=50)
    nlink = models.URLField()
    
    def __str__(self):
        return self.ntitle
    
class Xbox(models.Model):
    xtitle = models.CharField(max_length=120)
    ximage = models.ImageField()
    xprice = models.CharField(max_length=50)
    xlink = models.URLField()
    
    def __str__(self):
        return self.xtitle


class Playstation(models.Model):
    ptitle = models.CharField(max_length=120)
    pimage = models.ImageField()
    pprice = models.CharField(max_length=50)
    plink = models.URLField()
    
    def __str__(self):
        return self.ptitle


class ContactModel(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    phone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.email