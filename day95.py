import os, requests, json, openai, time, urllib
from requests.auth import HTTPBasicAuth

#------------ SET UP NEWSAI ---------------
country = 'gb'
url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={os.environ["newsapi"]}'

#------------ SET UP OPENAI ---------------
openai.api_key = os.environ["openai"]
openai.Model.list()

#------------ SET UP SPOTIFY --------------
spotID = os.environ['spotid']
spotSecret = os.environ['spotsecret']

spotUrl = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(spotID, spotSecret)

response = requests.post(spotUrl, data=data, auth=auth)
accessToken = response.json()['access_token']
headers = {'Authorization': f'Bearer {accessToken}'}

#------------ GET NEWS STORIES ------------
response = requests.get(url)
responseJson = response.json()


for counter in range(3):
  #Prep prompt
  prompt = f"Summarise {responseJson['articles'][counter]['url']} in two to three words."
  #Query OpenAI
  response2 = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens = 10)
  response2url = urllib.parse.quote(response2["choices"][0]["text"].replace("\n\n", ""))
  #Search Spotify
  spotSearch = f"https://api.spotify.com/v1/search?q=track:{response2url}&type=track&market={country}"
  spotResult = requests.get(spotSearch, headers=headers)
  print("Prompt: "+str(response2["choices"][0]["text"].replace("\n\n", "")))
  try:
    print("Song: "+spotResult.json()['tracks']['items'][0]['name'])
  except (KeyError, IndexError):
    pass
  try:
    print("Track: "+spotResult.json()['tracks']['items'][0]['url'])
  except (KeyError, IndexError):
    pass
  print()
  time.sleep(20)

