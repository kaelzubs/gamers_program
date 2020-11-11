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