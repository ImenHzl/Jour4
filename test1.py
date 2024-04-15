import requests
from bs4 import BeautifulSoup

url="https://fr.wikipedia.org/wiki/Test_(informatique)"
response = requests.get(url)
content= response.content
soup = BeautifulSoup(content, 'html.parser')
titre= soup.find("h1").text.split()
print(f"affiche titre: {titre}")
section=soup.find("div",class_="mw-body-content")
#print (f" liste de section : {section}")
for fils in  section.find_all("h2"):
    for div in fils:
            sousTitre=div.get("id")
            print(sousTitre)