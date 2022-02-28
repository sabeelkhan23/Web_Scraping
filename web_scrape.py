#CIS593 - BIG DATA
#SABEEL KHAN - CSUID:2829233
#METHOD2: Webpages as Unstructured Data with Parsing
#REFRENCE LINK: https://www.geeksforgeeks.org/working-csv-files-python/
#https://www.geeksforgeeks.org/wand-splice-function-python/#:~:text=The%20splice()%20function%20is,by%20the%20available%20background%20color.
#https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
#https://docs.python.org/3/library/sqlite3.html               

import requests
import csv
from bs4 import BeautifulSoup
import os
import sqlite3
from pathlib import Path

DB = Path("President_Speech.db")
conn = sqlite3.connect('President_Speech.db')
cursor = conn.cursor()
query = []

URL = "https://www.infoplease.com/homework-help/history/collected-state-union-addresses-us-presidents" 

request = requests.get(URL)
soup = BeautifulSoup(request.content, 'html.parser')
print(soup.prettify())
lists = soup.find('div', class_='toc')
count = 1
print(lists)

ALL_DATA = []
for list in lists.findAll('span', class_='article'):
    DATA = []
    Name = " "
    Date = " "
    get_name = list.a.text.split("(", 1)[0].replace('.', '').lower()
    Name = get_name.replace('-', '')
    get_date = list.a.text.split("(", 1)[1][:-1].replace(',', '').lower()
    Date = get_date.replace('-', '')
    y = "-"
    Link = list.a['href']

if Link[slice(3)] == '/t/' or Link[slice(3)] == '':
    Link = "/primary-sources/government/presidential-speeches/state-union-address-" + y.join(Name) 
    + y.join(Date)
        
else:
    Link = list.a['href']
    og_url = "https://www.infoplease.com"
    Link = og_url + Link
    DATA.append(Name)
    DATA.append(Date)
    DATA.append(Link)
    ALL_DATA.append(DATA)

file = os.path.join('C:\\Users\\sabee\\OneDrive\\Desktop\\Big_Data\\output', 'speech.csv')
with open(file, mode='w') as files:
        writer = csv.writer(files)
        writer.writerow(('Name', 'Date', 'Link'))
        for data in ALL_DATA:
            Name, Date, Link = data
            writer.writerow((Name, Date, Link))

try:
	cursor.execute('SELECT DISTINCT Name, Date, Link')
except Exception as f:
	print(f)
rows = cursor.fetchall()

conn.commit
conn.close
