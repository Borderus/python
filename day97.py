import requests, os, json
import openai
from bs4 import BeautifulSoup

#-------------OPENAI AUTH----------------

openai.api_key = os.environ['openai']
openai.Model.list()

#-------------OPENAI QUERY---------------

url = "https://en.wikipedia.org/wiki/Hair_loss"
prompt=f"Summarise {url} in 40 words."

response = openai.Completion.create(
  model = "text-davinci-003",
  prompt = prompt,
  temperature = 0.6,
  max_tokens = 100
)
summary = response["choices"][0]["text"][2:]

#-------------WIKI QUERY----------------

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
refs = soup.find_all("cite")

#------------PRINT OUT------------------

print(summary)
print()
print("References:")
for counter in range(len(refs)):
  print(str(counter+1)+": "+refs[counter].get_text())