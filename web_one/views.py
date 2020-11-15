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
    
    
#     title = driver.find_elements_by_xpath("//*[@title='Roblox Gift Card - 800 Robux [Online Game Code]']").text
    
#     list_price = driver.find_elements_by_xpath("//*[@class='ac-product-price']")
#     price = [p.text for p in list_price]
    
    # list_images = driver.find_elements_by_xpath("//*[@class='a-span2 product-image']")
    # images = []
    # for i in range(len(list_images)):
    # # this line produces StaleElementReferenceException
    #     WebDriverWait(driver, 30).until(EC.staleness_of(list_images[i]))
    #     image = list_images[i].find_element_by_tag_name('img')
    #     images.append(image.get_attribute('src'))
    
    # print(title, price)
    # links = []
    # for i in results:
    #     # this line produces StaleElementReferenceException
    #     WebDriverWait(driver, 30).until(EC.staleness_of(results[i]))
    #     link = results[i].get_attribute('href')
    #     links.append(link)
        
    # print(links)
    
    # results = driver.find_elements_by_xpath("//*[@class=' co-product-list__main-cntr']//*[@class=' co-item ']//*[@class='co-product']//*[@class='co-item__title-container']//*[@class='co-product__title']")
    # print('Number of results', len(results))
    # driver.quit()
   
# gamelist()


# def firstone():   
#     #Create your views here.
#     #Trending in Video Games
#     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
#     uri = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225016011&rh=n%3A%2116225016011%2Cp_89%3AXbox%7CXbox+360%7CXbox+One&dc&fst=as%3Aoff&pf_rd_i=16225016011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=03b28c2c-71e9-4947-aa06-f8b5dc8bf880&pf_rd_r=0F88GSY942XZVP0B1FD8&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1510597123&rnid=2528832011&ref=s9_acss_bw_cts_AEVNVIDE_T3_w'
#     res = requests.get(uri, headers=headers)
#     sup = BeautifulSoup(res.content, features='lxml')
#     # with open('trended.html', 'w') as file:
#     #     file.write("%s" % sup)
#     image = sup.find_all(class_="s-image")
#     titles = sup.find_all(class_="a-size-medium a-color-base a-text-normal")
#     price = sup.find_all(class_="a-offscreen")
#     linkz = sup.find_all(class_="a-link-normal s-no-outline")

    
#     imgarr = [img['src'] for img in image]
#     titlearr = [title.get_text() for title in titles]
#     pricearr = [p.get_text() for p in price]
#     linkarr = ["http://www.amazon.com" + links.get('href') + "?tag=kaelzubs-20" for links in linkz]
    

#     for img, title, priz, link in zip(imgarr, titlearr, pricearr, linkarr):
#         if not TrendModel.objects.filter(
#             timage=img,
#             ttitle=title,
#             tprice=priz,
#             tlink=link
#         ):
#             TrendModel.objects.create(
#                 ttitle=title,
#                 timage=img,
#                 tprice=priz,
#                 tlink=link
#             )
    
# firstone()


# def secondone():        
#     # Create your views here.
#     # Best Sellers in Video Games
#     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
#     url = 'https://www.amazon.com/b?node=18505457011&pd_rd_w=tKLAU&pf_rd_p=8e1f1374-e97f-4fa0-8041-0a82fa6f5859&pf_rd_r=XTR8MBM63KM0X4CN9HMM&pd_rd_r=0859fd57-fbe6-47bb-9356-36d6543be3b7&pd_rd_wg=buTPS'
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.content, features='lxml')

#     linkd = soup.find_all(class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")
#     images = soup.find_all(class_="s-access-image cfMarker")
#     prices = soup.find_all(class_="a-offscreen")
#     titles = soup.find_all(class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")
   
#     img_arr = [img['src'] for img in images]
#     title_arr = [title.get_text() for title in titles]
#     pricearr = [p.get_text() for p in prices]
#     linkarr = [links.get('href') + "?tag=kaelzubs-20" for links in linkd]

#     for img, title, priz, link in zip(img_arr, title_arr, pricearr, linkarr):
#         if not HomeModel.objects.filter(
#             title=title,
#             image=img,
#             price=priz
#         ):
#             HomeModel.objects.create(
#                 title=title,
#                 image=img,
#                 price=priz,
#                 link=link
#             )
        
# secondone()



def home_view(request):
    query = HomeModel.objects.all()[:24]
    llquery = HomeModel.objects.all()[15:22]
    lquery = HomeModel.objects.all()[10:17]
    mini = TrendModel.objects.all()[2:4]
    pquery = HomeModel.objects.all()
    tquery = TrendModel.objects.all()[1:4]
    rquery = RelatedModel.objects.all()
    ttquery = TrendModel.objects.all()[0:6]
    return render(request, 'base.html', {
        'query': query,
        'tquery': tquery,
        'mini': mini,
        'rquery': rquery,
        'lquery': lquery,
        'llquery': llquery,
        'pquery': pquery,
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



def handler404(request, exception, template_name="error_404.html"):
    
    return render(request, template_name)


def handler500(request, template_name="error_500.html"):
    
    return render(request, template_name)


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changfreq = 'daily'

    def items(self):
        return ['home', 'xbox', 'playstation', 'nintendo', 'accessories', ]

    def location(self, item):
        return reverse(item)
    
