import requests, random, time, json, threading, warnings, re, fnmatch, os
from selenium import webdriver
import cloudscraper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#browser = webdriver.Chrome(executable_path=r'C:\Users\Ruthless Economy PC\Desktop\Gemini Webdriver\chromedriver.exe')
scraper = cloudscraper.create_scraper()

count = 0
all = []
allprofile = []

head = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
}

while count < 5559:
    gate = 0
    progate = 0
    #10419

    count = str(count)
    URL = ("https://opensea.io/assets/0xd2f668a8461d6761115daf8aeb3cdf5f40c532c6/" + count)
    try:
        response = scraper.get(URL).text
    except:
        pass
    profile = re.findall("{\"quantity\":\"1\",\"owner\":{\"address\":\"(.*?)\",\"config\":", response)
    #placeholder = response.content.decode('utf-8')
    count = int(count)
    count = count + 1

    if len(profile) > 0:
        if profile[0] in allprofile:
            progate = 1

    if len(profile) > 0 and progate == 0:
        allprofile.append(profile[0])
        
        #time.sleep(3)
        try:
            response = scraper.get("https://opensea.io/" + profile[0]).text
        except:
            pass
        twitter = re.findall("\"twitterUsername\":\"(.*?)\",\"websiteUrl\"", response)

        twitter = list(dict.fromkeys((twitter)))
        twitter = str(twitter)
        twitter = twitter.replace("@", "")
        twitter = twitter.replace("'", "")
        twitter = twitter.replace("[", "")
        twitter = twitter.replace("]", "")
        print(URL, profile[0], twitter)

        if twitter in all:
            gate = 1

        all.append(twitter)
        all = list(dict.fromkeys((all)))

        if gate == 0:
            with open("NFT Twitter.txt", "a", encoding="utf-8") as finish:
                finish.write(twitter + "\n")
                finish.close()

print(all)



#browser.get("https://opensea.io/assets/acrocalypse")

#browser.get("https://opensea.io/collection/acrocalypse?tab=activity&search[isSingleCollection]=true&search[eventTypes][0]=AUCTION_CREATED")
#clean = browser.page_source
#print(clean)
#collections = re.findall(",\"slug\":\"(.*?)\",\"logo\"", clean)