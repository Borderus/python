import requests, urllib
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
myLines = soup.find_all("span", {"class":"titleline"})

myTitles = []
for item in myLines:
  contents=str(item).split(">")[2][0:-3]
  if contents.lower().find("google") != -1:
    myTitles.append(contents)

print(myTitles)