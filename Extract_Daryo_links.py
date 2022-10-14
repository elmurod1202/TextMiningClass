import requests
import lxml.html
import time
import random

#Creating a text file to write all the article links:
f = open("daryo-uz-links.txt", "w")
#Going through all the Daryo news home pages(10 article titles per homepage):
website_address = 'https://m.daryo.uz/'
max_number_pages = 23864


for page in range(1,2):
    time.sleep(random.randint(1,3))
    url=website_address+"page/"+str(page)+"/"
    print("New page URL:",url)
    #Sending request and obtaining response:
    response = requests.get(url)
    # Check the response if the web server returned a normal answer:
    if (response.status_code == 200):
        print("Response OK!")
        # Converting the response to lxml format:
        webpage = lxml.html.fromstring(response.content)

        #Extracting the links:
        #Thje XPath of the link:  //*[@id="content"]/div[1]/ul/li[1]/a
        links = webpage.xpath('//*[@id="content"]/div[1]/ul/li/a')
        for link_a in links:
            link = website_address + link_a.attrib['href']
            print("Found a new link: ",link)
            f.write(link)
            f.write("\n")
    else:
        print("ERROR requesting the web page!")
print("Done extracting links from the website")
#Closing the links file:
f.close()

    