import requests, json
from replit import db

menu = ''

#------------NEW JOKE-------------
def newjoke():
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
  
  joke = result.json()
  return joke

def loadjokes():
  for key, value in db.items():
      result = requests.get("https://icanhazdadjoke.com/j/"+value['id'], headers={"Accept":"application/json"})
      print(result.json()['joke'])

while True:
  if menu != 'l':
    joke = newjoke()
    print(joke['joke'])
  menu = input("\n(s)ave joke, (l)oad old jokes, (n)ew joke, (q)uit.\n")
  if menu == 's' and joke['id'] != '':
    newkey=0
    for key in db.keys():
      try:
        newkey = max(int(key), int(newkey))
      except ValueError:
        pass
    newkey = str(newkey+1).zfill(5)
    db[newkey] = {'id': joke['id']}
  elif menu == 'l':
    loadjokes()
  elif menu == 'q':
    break

#How do you get two whales in a car? Start in England and drive West.