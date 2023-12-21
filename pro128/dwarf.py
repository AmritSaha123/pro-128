from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []
page = requests.get(START_URL)
soup = bs(page.text,"html.parser")
star_table = soup.find_all("table",{"class":"wikitable sortable"})
totaltables = len(star_table)
templist = []
table_rows = star_table[1].find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    templist.append(row)
starnames = []
distance = []
mass = []
radius = []
print(templist)
for i in range(1,len(templist)):
    starnames.append(templist[i][0])
    distance.append(templist[i][5])
    mass.append(templist[i][7])
    radius.append(templist[i][8])
headers = ["starname","distance","mass","radius"]
df2 = pd.DataFrame(list(zip(starnames,distance,mass,radius)),columns=headers)
print(df2)
df2.to_csv("main.csv")