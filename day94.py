import requests, json, os, time
import openai

openai.api_key = os.environ['openai']
openai.Model.list()

country = 'gb'

url = (f'https://newsapi.org/v2/top-headlines?'
       f'country={country}&'
       f'apiKey={os.environ["newsapi"]}')
response = requests.get(url)

articleCount = 5

for item in response.json()['articles']:
  prompt = f"Summarise this story: {item['url']}"
  response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=100)
  print(item['title'])
  print(response['choices'][0]['text'])
  print('\n\n')
  time.sleep(20)