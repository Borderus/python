import requests
from bs4 import BeautifulSoup

pageSuffix = [""]
for counter in range(2, 51):
  pageSuffix.append("/catalogue/page-"+str(counter).strip()+".html")

items = {}

#Loop through pages and scrape pages
for suffix in pageSuffix:
  url = "http://books.toscrape.com"+suffix

  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')

  myLines = soup.find_all("article", {"class": "product_pod"})
  for entry in myLines:

    rawtitle = entry.find_all("h3")
    title = str(rawtitle).split('"')[3]

    rawprice = entry.find_all("p", {"class": "price_color"})
    price = float(str(rawprice).split('>')[1][2:-3])

    rawurl = entry.find_all("h3")
    url = "http://books.toscrape.com/"+str(rawurl).split('"')[1]

    items[title] = {"price": price, "url": url}

#Print out findings
for item, dict in items.items():
  print(item)
  print("£"+"{:.2f}".format(dict["price"]).strip())
  print(dict["url"])
  print()