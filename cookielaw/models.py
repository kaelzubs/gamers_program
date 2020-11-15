from django.db import models


# Create your models here.

class cookie_Page(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    price = models.CharField(max_length=50)
    link = models.URLField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
