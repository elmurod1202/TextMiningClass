import requests
import lxml.html

#the required first parameter of the 'get' method is the 'url':

# Requesting the webpage contents from the web:
url = 'https://m.daryo.uz/2022/09/30/suriyaning-10-ta-viloyatida-vabo-avj-oldi-va-butun-mamlakat-boylab-tarqalmoqda/'
url2 = 'https://m.daryo.uz/2022/09/30/qishloq-xojaligi-sohasida-oquv-tajriba-xojaliklari-tashkil-etiladi/'
url3 = 'https://m.daryo.uz/2022/10/14/ozbekistonda-dam-olish-kunlari-quruq-va-iliq-ob-havo-boladi/'
response = requests.get(url3)

#Check the response if the web server returned a normal answer:
if(response.status_code ==200):
    print("Response OK!")
    #Converting the response to lxml format:
    webpage = lxml.html.fromstring(response.content)
    
    #Extracting the title of the article:
    article_title_div = webpage.xpath('//*[@id="content"]/div[1]/h1')
    article_title = article_title_div[0].text
    print("Title: ",article_title)

    #Extracting necessary text:
    article_paragraphs = webpage.xpath('//*[@id="content"]/div[1]/div[3]/p')
    for article_text in article_paragraphs:
        print(article_text.text)
else:
    print("ERROR requesting the web page!")

    