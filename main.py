#Kindly refrain changing credits
#Its no rocket sceince , you can code it too


import requests
from bs4 import BeautifulSoup

print('''

█▀ █▀▀ █▀█ ▄▀█ █▀█ █ █▀█ █░█ █▀
▄█ █▄▄ █▀▄ █▀█ █▀▀ █ █▄█ █▄█ ▄█
      [+]Author: https://github.com/ShantanuRauthan

''')

print("Enter the Website URL with http/https: ")
url = input()

r= requests.get(url)
r.raise_for_status()

soup = BeautifulSoup(r.text,'html.parser')

anchor = soup.find_all('a')


def LinkScraper():
  LinkSet = set()

  for link in  anchor:

    if (link.get('href')!= '#'):
      LinkSet = (link.get('href'))
      print(LinkSet)
      with open ('Links.txt','a') as f:
         f.write(LinkSet + "\n")
      f.close
      

LinkScraper()
