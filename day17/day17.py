# web scrapping 

'''
try working
try:
    a= 1/0
    print(a)
except Exception as e:
    print("pleachage change the value by 0")
    print(e)'
'''

import time
import sys
from bs4 import BeautifulSoup
import requests

'''
try:
    page=requests.get('https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database/2022')

except Exception as e:
         print(e)'''
    
time.sleep(2)

soup=BeautifulSoup(page.text,'html.parser')
links=soup.find_all('div',attrs={'class' :'arrowed-link'})

# page


soup

links

data_link=soup.find_all('div',attrs={'class' :'arrowed-link'})

links[0]

links[0].text


links[0].a

data_link=links[0].a['href']

data_link



