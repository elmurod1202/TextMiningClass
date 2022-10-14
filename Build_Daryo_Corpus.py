import requests
import lxml.html
import time
import random

print("Starting corpus collection.")
#Creating a text file to write all the article links:
f = open("daryo_corpus.txt", "a")
#Going through all the Daryo news articles:
website_address = 'https://m.daryo.uz/'

#Opening links file and running through it:
with open("daryo-uz-links.txt") as links_file:
    for line in links_file:
        url = line.strip()
        #Respecting the server:
        time.sleep(random.randint(1, 3))
        # Requesting the webpage contents from the web:
        print("Requesting url: ",url)
        response = requests.get(url)
        # Check the response if the web server returned a normal answer:
        if (response.status_code == 200):
            print("Response OK!")
            # Converting the response to lxml format:
            webpage = lxml.html.fromstring(response.content)

            # Extracting the title of the article:
            article_title_div = webpage.xpath('//*[@id="content"]/div[1]/h1')
            article_title = article_title_div[0].text
            print("Title: ", article_title)
            f.write(article_title)
            f.write("\n")

            # Extracting necessary text:
            article_paragraphs = webpage.xpath('//*[@id="content"]/div[1]/div[3]/p')
            for article_text in article_paragraphs:
                f.write(str(article_text.text))
            f.write("\n")
        else:
            print("ERROR requesting the web page!")

print("Finished collecting corpus.")

#Closing the corpus file:
f.close()
