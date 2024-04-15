import requests
from bs4 import BeautifulSoup

url="https://www.marc-orian.com/fr_FR/c/bijoux/par-type/bracelets/bracelets-chaines/facette/femme/"
response = requests.get(url)
content= response.content
soup = BeautifulSoup(content, 'html.parser')
section=soup.findAll("div",class_="c-grid__item c-grid__item")
#print (f" liste de section : {section}")

for elt in section:
    prix= section[3] 
print(prix)

