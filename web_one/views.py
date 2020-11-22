from bs4 import BeautifulSoup
from django.db.models import query
from django.db.models.fields import files
import requests
from django.shortcuts import render, redirect
from requests.api import request
from .models import HomeModel, TrendModel, RelatedModel, Accessories, Nintendo, Xbox, Playstation
from newsletter.forms import EmailSignupForm
from .forms import ContactForms
from django.core.mail import send_mail, get_connection
from django.contrib import sitemaps
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .secretKey.config import keys
# import libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time, ssl




# def accessories():
    
#     # For ignoring SSL certificate errors
#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE
    
#     # specify the url
#     urlpage = 'https://affiliate-program.amazon.com/home/productlinks/search/?category=gamedownloads&keywords=accessories&sortby='
    
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
#     time.sleep(120)
    
#     title_arr = []
#     list_title = driver.find_elements(By.TAG_NAME, 'a')
#     for tit in list_title:
#         title = tit.get_attribute('title')
#         href = tit.get_attribute("href")
#         if 'tag=kaelzubs-20' not in href:
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
#         alt = img.get_attribute('alt')
#         if 'B0' not in alt:
#             continue
#         image_arr.append(images)
            
    
#     for imag, titl, prize, linc in zip(image_arr, title_arr, price_arr, link_arr):
#         if not Accessories.objects.filter(
#             atitle=titl,
#             aimage=imag,
#             aprice=prize,
#             alink=linc
#         ):
#             Accessories.objects.create(
#                 atitle=titl,
#                 aimage=imag,
#                 aprice=prize,
#                 alink=linc
#             )
    
#     driver.quit()
   
# accessories()



# def nintendo():
    
#     # For ignoring SSL certificate errors
#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE
    
#     # specify the url
#     urlpage = 'https://affiliate-program.amazon.com/home/productlinks/search/?category=gamedownloads&keywords=nintendo&sortby='
    
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
#     time.sleep(120)
    
#     title_arr = []
#     list_title = driver.find_elements(By.TAG_NAME, 'a')
#     for tit in list_title:
#         title = tit.get_attribute('title')
#         href = tit.get_attribute("href")
#         if 'tag=kaelzubs-20' not in href:
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
#         alt = img.get_attribute('alt')
#         if 'B0' not in alt:
#             continue
#         image_arr.append(images)

    
#     for imag, titl, prize, linc in zip(image_arr, title_arr, price_arr, link_arr):
#         if not Nintendo.objects.filter(
#             ntitle=titl,
#             nimage=imag,
#             nprice=prize,
#             nlink=linc
#         ):
#             Nintendo.objects.create(
#                 ntitle=titl,
#                 nimage=imag,
#                 nprice=prize,
#                 nlink=linc
#             )
    
#     driver.quit()
   
# nintendo()




# def xbox():
    
#     # For ignoring SSL certificate errors
#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE
    
#     # specify the url
#     urlpage = 'https://affiliate-program.amazon.com/home/productlinks/search/?category=gamedownloads&keywords=xbox&sortby='
    
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
#     time.sleep(120)
    
#     title_arr = []
#     list_title = driver.find_elements(By.TAG_NAME, 'a')
#     for tit in list_title:
#         title = tit.get_attribute('title')
#         href = tit.get_attribute("href")
#         if 'tag=kaelzubs-20' not in href:
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
#         alt = img.get_attribute('alt')
#         if 'B0' not in alt:
#             continue
#         image_arr.append(images)

    
#     for imag, titl, prize, linc in zip(image_arr, title_arr, price_arr, link_arr):
#         if not Xbox.objects.filter(
#             xtitle=titl,
#             ximage=imag,
#             xprice=prize,
#             xlink=linc
#         ):
#             Xbox.objects.create(
#                 xtitle=titl,
#                 ximage=imag,
#                 xprice=prize,
#                 xlink=linc
#             )
    
#     driver.quit()
   
# xbox()



# def playstation():
    
#     # For ignoring SSL certificate errors
#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE
    
#     # specify the url
#     urlpage = 'https://affiliate-program.amazon.com/home/productlinks/search/?category=gamedownloads&keywords=playstation&sortby='
    
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
#     time.sleep(120)
    
#     title_arr = []
#     list_title = driver.find_elements(By.TAG_NAME, 'a')
#     for tit in list_title:
#         title = tit.get_attribute('title')
#         href = tit.get_attribute("href")
#         if 'tag=kaelzubs-20' not in href:
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
#         alt = img.get_attribute('alt')
#         if 'B0' not in alt:
#             continue
#         image_arr.append(images)

    
#     for imag, titl, prize, linc in zip(image_arr, title_arr, price_arr, link_arr):
#         if not Playstation.objects.filter(
#             ptitle=titl,
#             pimage=imag,
#             pprice=prize,
#             plink=linc
#         ):
#             Playstation.objects.create(
#                 ptitle=titl,
#                 pimage=imag,
#                 pprice=prize,
#                 plink=linc
#             )
    
#     driver.quit()
   
# playstation()






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
#     time.sleep(120)
    
#     title_arr = []
#     list_title = driver.find_elements(By.TAG_NAME, 'a')
#     for tit in list_title:
#         title = tit.get_attribute('title')
#         href = tit.get_attribute("href")
#         if 'tag=kaelzubs-20' not in href:
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
#         alt = img.get_attribute('alt')
#         if 'B0' not in alt:
#             continue
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
#     time.sleep(120)
    
#     title_arr = []
#     list_title = driver.find_elements(By.TAG_NAME, 'a')
#     for tit in list_title:
#         title = tit.get_attribute('title')
#         href = tit.get_attribute("href")
#         if 'tag=kaelzubs-20' not in href:
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
#         alt = img.get_attribute('alt')
#         if 'B0' not in alt:
#             continue
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
#         href = tit.get_attribute("href")
#         if 'tag=kaelzubs-20' not in href:
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
#         alt = img.get_attribute('alt')
#         if 'B0' not in alt:
#             continue
#         image_arr.append(images)

    
#     for imag, titl, prize, linc in zip(image_arr, title_arr, price_arr, link_arr):
#         if not TrendModel.objects.filter(
#             ttitle=titl,
#             timage=imag,
#             tprice=prize,
#             tlink=linc
#         ):
#             TrendModel.objects.create(
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
    medquery = RelatedModel.objects.all()[:2]
    
    trendquery = TrendModel.objects.all()
    
    salequery = RelatedModel.objects.all()[2:7]
    bestquery = RelatedModel.objects.all()[7:13]
    viewquery = RelatedModel.objects.all()[14:19]
    
    paginator = Paginator(query, 36)
    page = request.GET.get('page')
    try:
        pagpages = paginator.page(page)
    except PageNotAnInteger:
        pagpages = paginator.page(1)
    except EmptyPage:
        pagpages = paginator.page(paginator.num_pages)
        
    
    form = EmailSignupForm()
        
    return render(request, 'base.html', {
        'pagpages': pagpages,
        'topquery': topquery,
        'bestquery': bestquery,
        'trendquery': trendquery,
        'viewquery': viewquery,
        'salequery': salequery,
        'medquery': medquery,
            
        'form': form,
    })



def xbox_view(request):
    xbxquery = Xbox.objects.all()
    paginator = Paginator(xbxquery, 36)
    page = request.GET.get('page')
    try:
        pagpages = paginator.page(page)
    except PageNotAnInteger:
        pagpages = paginator.page(1)
    except EmptyPage:
        pagpages = paginator.page(paginator.num_pages)
    form = EmailSignupForm()
    return render(request, 'xbox.html', {
        'form': form,
        'pagpages': pagpages,
        'xbxquery': xbxquery,
    })
    
def playstation_view(request):
    playquery = Playstation.objects.all()
    paginator = Paginator(playquery, 36)
    page = request.GET.get('page')
    try:
        pagpages = paginator.page(page)
    except PageNotAnInteger:
        pagpages = paginator.page(1)
    except EmptyPage:
        pagpages = paginator.page(paginator.num_pages)
    form = EmailSignupForm()
    return render(request, 'playstation.html', {
        'form': form,
        'pagpages': pagpages,
        'playquery': playquery,
    })
    
def nintendo_view(request):
    ninquery = Nintendo.objects.all()
    paginator = Paginator(ninquery, 36)
    page = request.GET.get('page')
    try:
        pagpages = paginator.page(page)
    except PageNotAnInteger:
        pagpages = paginator.page(1)
    except EmptyPage:
        pagpages = paginator.page(paginator.num_pages)
    form = EmailSignupForm()
    return render(request, 'nintendo.html', {
        'form': form,
        'pagpages': pagpages,
        'ninquery': ninquery,
    })
    
def accessories_view(request):
    accquery = Accessories.objects.all()
    paginator = Paginator(accquery, 36)
    page = request.GET.get('page')
    try:
        pagpages = paginator.page(page)
    except PageNotAnInteger:
        pagpages = paginator.page(1)
    except EmptyPage:
        pagpages = paginator.page(paginator.num_pages)
    form = EmailSignupForm()
    return render(request, 'accessories.html', {
        'form': form,
        'pagpages': pagpages,
        'accquery': accquery,
    })
    
    
def about_view(request):
    form = EmailSignupForm()
    return render(request, 'about.html', {'form': form})
    
    
def contact_view(request):

    submitted = False
    if request.method == 'POST':
        forms = ContactForms(request.POST or None )
        if forms.is_valid():
            cd = forms.cleaned_data
            con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@gameshopa.com'),
                ['kaelzubs@gmail.com'],
                cd['name'],
                cd['phone'],
                connection=con
            )
            return redirect('contact_success')
    else:
        forms = ContactForms()
        if 'submitted' in request.GET:
            submitted = True
    
    form = EmailSignupForm()

    return render(request, 'contact.html', {'form': form, 'forms': forms})
    

def contact_success(request):
    form = EmailSignupForm()
    return render(request, 'contact_success.html', {'form': form})

  
def disclaimer_view(request):
    form = EmailSignupForm()
    return render(request, 'disclaimer.html', {'form': form})

def search_view(request):
    searchpages = HomeModel.objects.all()
    paginator = Paginator(searchpages, 28)
    page = request.GET.get('page')
    try:
        pagpages = paginator.page(page)
    except PageNotAnInteger:
        pagpages = paginator.page(1)
    except EmptyPage:
        pagpages = paginator.page(paginator.num_pages)
    query = request.GET.get('q')
    if query:
        pagpages = HomeModel.objects.filter(
            Q(title__icontains=query) |
            Q(image__icontains=query) |
            Q(price__icontains=query) |
            Q(link__icontains=query)
        ).distinct()
        
    form = EmailSignupForm()

    return render(request, 'search.html', {'form': form, 'pagpages': pagpages})

def handler404(request, exception, template_name="error_404.html"):
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
    
