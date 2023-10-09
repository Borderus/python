#---------------SET UP-----------------
import requests, json, os
from requests.auth import HTTPBasicAuth

from flask import Flask, request, redirect, session
app = Flask(__name__, static_url_path = '/static')
app.secret_key=os.environ['sessionKey']

#----------------AUTH------------------
clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

url="https://accounts.spotify.com/api/token"
data={"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)
accessToken = response.json()['access_token']

#--------------MAIN PAGE---------------

@app.route('/')
def index():
  f = open('mainpage.html', 'r')
  page = f.read()
  f.close()

  f = open('record.html', 'r')
  entry = f.read()
  f.close()
  try:
    for key, value in session["songlist"].items():
      newEntry = entry.replace("{TRACK}", value["track"])
      newEntry = newEntry.replace("{ARTIST}", value["artist"])
      newEntry = newEntry.replace("{ID}", value["id"])
      page += newEntry
  except KeyError:
    print("Error here")
    pass
  
  return page

#------------DEFINE SONGS--------------
@app.route('/getSongs', methods=['POST'])
def getSongs():
  form = request.form
  year = form["year"]
  url = f"https://api.spotify.com/v1/search?q=year:{year}&type=track&market=GB"
  headers = {'Authorization': f'Bearer {accessToken}'}

  response = requests.get(url, headers=headers)

  songlist = {}
  for entry in response.json()['tracks']['items']:
    songlist[entry['id']] = {'track':(entry['name']), 'artist':(entry['artists'][0]['name']), 'id':(entry['id'])}
  session["songlist"] = songlist
  return redirect('/')

app.run(host='0.0.0.0', port=81)