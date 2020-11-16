from bs4 import BeautifulSoup
from django.db.models import query
from django.db.models.fields import files
import requests
from django.shortcuts import render
from requests.api import request
from .models import HomeModel, TrendModel, RelatedModel

from django.contrib import sitemaps
from django.urls import reverse

from .secretKey.config import keys
# import libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time, ssl
# import pandas as pd


            

# def gamelist():
    
#     # For ignoring SSL certificate errors
#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE
    
#     # specify the url
#     urlpage = 'https://affiliate-program.amazon.com/home/productlinks/search?ac-ms-src=ac-nav&category=gamedownloads&keywords=&sortby=&subcategory=20972781011'
    
#     # run firefox webdriver from executable path of your choice
#     driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

#     # get web page
#     driver.get(urlpage)
    
#     # login username
#     email = driver.find_element_by_id("ap_email")
#     email.clear()
#     email.send_keys(keys['username'])

#     # login password
#     password = driver.find_element_by_id("ap_password")
#     password.clear()
#     password.send_keys(keys['password'])
        
#     # signInSubmit
#     driver.find_element_by_id("signInSubmit").click()
    
#     # execute script to scroll down the page
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    
#     # sleep for 30s
#     time.sleep(30)
    
#     title_arr = []
#     list_title = driver.find_elements(By.TAG_NAME, 'a')
#     for tit in list_title:
#         title = tit.get_attribute('title')
#         if '[' not in title:
#             continue
#         title_arr.append(title)
    
    
#     link_arr = []
#     list_link = driver.find_elements(By.TAG_NAME, 'a')
#     for lk in list_link:
#         link = lk.get_attribute('href')
#         if 'tag=kaelzubs-20' not in link:
#             continue
#         link_arr.append(link)
    
#     price_arr = []
#     list_price = driver.find_elements_by_xpath("//*[@class='ac-product-price']")
#     for price in list_price:
#         priz = price.text
#         price_arr.append(priz)
    
    
#     image_arr = []
#     list_images = driver.find_elements(By.TAG_NAME, 'img')
#     for img in list_images:
#         images = img.get_attribute('src')
#         if '.jpg' not in images:
#             if '91Vk1mS1x3L._SL500_.png' not in images:
#                 continue
#         image_arr.append(images)

    
#     for imag, titl, prize, linc in zip(image_arr, title_arr, price_arr, link_arr):
#         if not HomeModel.objects.filter(
#             title=titl,
#             image=imag,
#             price=prize,
#             link=linc
#         ):
#             HomeModel.objects.create(
#                 title=titl,
#                 image=imag,
#                 price=prize,
#                 link=linc
#             )
    
#     driver.quit()
   
# gamelist()


# def gamelistonline():
    
#     # For ignoring SSL certificate errors
#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE
    
#     # specify the url
#     urlpage = 'https://affiliate-program.amazon.com/home/productlinks/search/?category=gamedownloads&subcategory=17596052011&keywords=sale&sortby='
    
#     # run firefox webdriver from executable path of your choice
#     driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

#     # get web page
#     driver.get(urlpage)
    
#     # login username
#     email = driver.find_element_by_id("ap_email")
#     email.clear()
#     email.send_keys(keys['username'])

#     # login password
#     password = driver.find_element_by_id("ap_password")
#     password.clear()
#     password.send_keys(keys['password'])
        
#     # signInSubmit
#     driver.find_element_by_id("signInSubmit").click()
    
#     # execute script to scroll down the page
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    
#     # sleep for 30s
#     time.sleep(30)
    
#     title_arr = []
#     list_title = driver.find_elements(By.TAG_NAME, 'a')
#     for tit in list_title:
#         title = tit.get_attribute('title')
#         if '[' not in title:
#             continue
#         title_arr.append(title)
    
    
#     link_arr = []
#     list_link = driver.find_elements(By.TAG_NAME, 'a')
#     for lk in list_link:
#         link = lk.get_attribute('href')
#         if 'tag=kaelzubs-20' not in link:
#             continue
#         link_arr.append(link)
    
#     price_arr = []
#     list_price = driver.find_elements_by_xpath("//*[@class='ac-product-price']")
#     for price in list_price:
#         priz = price.text
#         price_arr.append(priz)
    
    
#     image_arr = []
#     list_images = driver.find_elements(By.TAG_NAME, 'img')
#     for img in list_images:
#         images = img.get_attribute('src')
#         if '.jpg' not in images:
#             if '91Vk1mS1x3L._SL500_.png' not in images:
#                 continue
#         image_arr.append(images)

    
#     for imag, titl, prize, linc in zip(image_arr, title_arr, price_arr, link_arr):
#         if not RelatedModel.objects.filter(
#             rtitle=titl,
#             rimage=imag,
#             rprice=prize,
#             rlink=linc
#         ):
#             RelatedModel.objects.create(
#                 rtitle=titl,
#                 rimage=imag,
#                 rprice=prize,
#                 rlink=linc
#             )
    
#     driver.quit()
   
# gamelistonline()




# def gamelistonlinetrend():
    
#     # For ignoring SSL certificate errors
#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE
    
#     # specify the url
#     urlpage = 'https://affiliate-program.amazon.com/home/productlinks/search/?category=videogames&subcategory=19497043011&keywords=&sortby='
    
#     # run firefox webdriver from executable path of your choice
#     driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

#     # get web page
#     driver.get(urlpage)
    
#     # login username
#     email = driver.find_element_by_id("ap_email")
#     email.clear()
#     email.send_keys(keys['username'])

#     # login password
#     password = driver.find_element_by_id("ap_password")
#     password.clear()
#     password.send_keys(keys['password'])
        
#     # signInSubmit
#     driver.find_element_by_id("signInSubmit").click()
    
#     # execute script to scroll down the page
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    
#     # sleep for 30s
#     time.sleep(60)
    
#     title_arr = []
#     list_title = driver.find_elements(By.TAG_NAME, 'a')
#     for tit in list_title:
#         title = tit.get_attribute('title')
#         if '[' not in title:
#             continue
#         title_arr.append(title)
    
    
#     link_arr = []
#     list_link = driver.find_elements(By.TAG_NAME, 'a')
#     for lk in list_link:
#         link = lk.get_attribute('href')
#         if 'tag=kaelzubs-20' not in link:
#             continue
#         link_arr.append(link)
    
#     price_arr = []
#     list_price = driver.find_elements_by_xpath("//*[@class='ac-product-price']")
#     for price in list_price:
#         priz = price.text
#         price_arr.append(priz)
    
    
#     image_arr = []
#     list_images = driver.find_elements(By.TAG_NAME, 'img')
#     for img in list_images:
#         images = img.get_attribute('src')
#         if '.jpg' not in images:
#             if '91Vk1mS1x3L._SL500_.png' not in images:
#                 continue
#         image_arr.append(images)

    
#     for imag, titl, prize, linc in zip(image_arr, title_arr, price_arr, link_arr):
#         if not RelatedModel.objects.filter(
#             ttitle=titl,
#             timage=imag,
#             tprice=prize,
#             tlink=linc
#         ):
#             RelatedModel.objects.create(
#                 ttitle=titl,
#                 timage=imag,
#                 tprice=prize,
#                 tlink=linc
#             )
    
#     driver.quit()
   
# gamelistonlinetrend()




def home_view(request):
    query = HomeModel.objects.all()[4:]
    topquery = HomeModel.objects.all()[:3]
    
    salequery = RelatedModel.objects.all()[2:7]
    bestquery = RelatedModel.objects.all()[7:13]
    viewquery = RelatedModel.objects.all()[14:20]
    
    tquery = TrendModel.objects.all()[1:4]
    rquery = RelatedModel.objects.all()
    ttquery = TrendModel.objects.all()[0:6]
    return render(request, 'base.html', {
        'query': query,
        'topquery': topquery,
        'bestquery': bestquery,
        'viewquery': viewquery,
        'salequery': salequery,
        'ttquery': ttquery
    })


def xbox_view(request):
    return render(request, 'xbox.html')
    
def playstation_view(request):
    return render(request, 'playstation.html')
    
def nintendo_view(request):
    return render(request, 'nintendo.html')
    
def accessories_view(request):
    return render(request, 'accessories.html')
    
    
def about_view(request):
    return render(request, 'about.html')
    
    
def contact_view(request):
    return render(request, 'contact.html')
    
    
def disclaimer_view(request):
    return render(request, 'disclaimer.html')



def handler404(request, template_name="error_404.html"):
    
    return render(request, template_name, status=404)


def handler500(request, template_name="error_500.html"):

    return render(request, template_name, status=500)


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changfreq = 'daily'

    def items(self):
        return ['home', 'xbox', 'playstation', 'nintendo', 'accessories', ]

    def location(self, item):
        return reverse(item)
    
