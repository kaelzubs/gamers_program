from bs4 import BeautifulSoup
from django.db.models.fields import files
import time, random
import requests
from django.shortcuts import render
from .models import HomeModel, TrendModel, RelatedModel

def firstone():   
    #Create your views here.
    #Trending in Video Games
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    uri = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225016011&rh=n%3A%2116225016011%2Cp_89%3AXbox%7CXbox+360%7CXbox+One&dc&fst=as%3Aoff&pf_rd_i=16225016011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=03b28c2c-71e9-4947-aa06-f8b5dc8bf880&pf_rd_r=0F88GSY942XZVP0B1FD8&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1510597123&rnid=2528832011&ref=s9_acss_bw_cts_AEVNVIDE_T3_w'
    # proxies_list = ["128.199.109.241:8080","113.53.230.195:3128","125.141.200.53:80","125.141.200.14:80","128.199.200.112:138","149.56.123.99:3128","128.199.200.112:80","125.141.200.39:80","134.213.29.202:4444"]
    # proxies = {'https': random.choice(proxies_list)}
    # time.sleep(0.5 * random.random())
    res = requests.get(uri, headers=headers)
    sup = BeautifulSoup(res.content, features='lxml')
    # with open('trended.html', 'w') as file:
    #     file.write("%s" % sup)
    image = sup.find_all(class_="s-image")
    titles = sup.find_all(class_="a-size-medium a-color-base a-text-normal")
    price = sup.find_all(class_="a-offscreen")
    linkz = sup.find_all(class_="a-link-normal s-no-outline")

    
    imgarr = [img['src'] for img in image]
    titlearr = [title.get_text() for title in titles]
    pricearr = [p.get_text() for p in price]
    linkarr = ["http://www.amazon.com" + links.get('href') + "?tag=kaelzubs-20" for links in linkz]
    

    for img, title, priz, link in zip(imgarr, titlearr, pricearr, linkarr):
        if not TrendModel.objects.filter(
            timage=img,
            ttitle=title,
            tprice=priz,
            tlink=link
        ):
            TrendModel.objects.create(
                ttitle=title,
                timage=img,
                tprice=priz,
                tlink=link
            )
    
firstone()


def secondone():        
    # Create your views here.
    # Best Sellers in Video Games
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    url = 'https://www.amazon.com/b?node=18505457011&pd_rd_w=tKLAU&pf_rd_p=8e1f1374-e97f-4fa0-8041-0a82fa6f5859&pf_rd_r=XTR8MBM63KM0X4CN9HMM&pd_rd_r=0859fd57-fbe6-47bb-9356-36d6543be3b7&pd_rd_wg=buTPS'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, features='lxml')

    linkd = soup.find_all(class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")
    images = soup.find_all(class_="s-access-image cfMarker")
    prices = soup.find_all(class_="a-offscreen")
    titles = soup.find_all(class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")
   
    img_arr = [img['src'] for img in images]
    title_arr = [title.get_text() for title in titles]
    pricearr = [p.get_text() for p in prices]
    linkarr = [links.get('href') + "?tag=kaelzubs-20" for links in linkd]

    for img, title, priz, link in zip(img_arr, title_arr, pricearr, linkarr):
        if not HomeModel.objects.filter(
            title=title,
            image=img,
            price=priz
        ):
            HomeModel.objects.create(
                title=title,
                image=img,
                price=priz,
                link=link
            )
        
secondone()


def thirdone():        
    # Create your views here.
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    url = 'https://www.amazon.com/s?i=videogames-intl-ship&bbn=16225016011&rh=n%3A%2116225016011%2Cp_36%3A-3000&pd_rd_r=4beb8828-9bcf-406b-b969-d5089678ff19&pd_rd_w=U61z8&pd_rd_wg=oaEKa&pf_rd_p=1f552c7a-1af2-4608-bc6f-ba06ca3c43ac&pf_rd_r=DYSYW5SC4JD09N33K5RC&qid=1570809434&rnid=386453011'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, features='lxml')
    # with open('file.html', 'w') as file:
    #     file.write("%s" % soup)
    images = soup.find_all(class_="s-image")
    prices = soup.find_all(class_="a-price")[0]
    titles = soup.find_all(class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
   
    img_arr = [img['src'] for img in images]
    title_arr = [title.get_text() for title in titles]
    pricearr = [p.get_text() for p in prices]

    for img, title, priz in zip(img_arr, title_arr, pricearr):
        if not RelatedModel.objects.filter(
            rtitle=title,
            rimage=img,
            rprice=priz
        ):
            RelatedModel.objects.create(
                rtitle=title,
                rimage=img,
                rprice=priz,
            )
        
thirdone()


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
