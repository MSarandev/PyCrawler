import requests
import time
import os
from urllib import urlretrieve
from bs4 import BeautifulSoup

print("YOU NEED BEAUTIFULSOUP TO RUN THIS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Provided as is. Have fun.")
print("")
print("")

def_web = raw_input("Enter URL: ")

if("http" not in def_web):
    def_web = "http://" + def_web

count = 0

res = requests.get(def_web)
data = res.text

soup = BeautifulSoup(data, "html.parser")

print("")
print("")
print("~~SELECTOR~~")
print("1. 4chan")
print("SOON - Tumblr")
print("SOON - Reddit")
print("SOON - Google")
print("")
print("")


q_time = raw_input("What are we scraping?: ")

dir_me = "img_"+str(int(round(time.time() * 1000)))
os.makedirs(dir_me)

if(q_time == "1"):
    for link in soup.find_all("a", class_="fileThumb"):
        ext_1 = str(link.get('href'))
        if("webm" not in ext_1):
            ext_1 = "." + ext_1[-3:]
        else:
            ext_1 = "." + ext_1[-4:]

        print("http:"+link.get('href'))
        urlretrieve("http:"+link.get('href'), dir_me+"/"+str(int(round(time.time() * 1000)))+ext_1)
        count += 1
        print(">> SAVED")
        print(">> COUNT: " + str(count))


else:
    print("NOT YET SUPPORTED")


if(count != 0):
    print ("DONE")