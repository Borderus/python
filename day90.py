import requests

for count in range(10):
  result = requests.get("https://randomuser.me/api")
  user = result.json()
  #print(json.dumps(user, indent=2))
  for person in user['results']:
    namedict = person['name']
    name = namedict['first']+" "+namedict['last']

    print(name)

    #Get picture
    image = person["picture"]['large']
    picture = requests.get(image)
    f = open("images/image_"+namedict['last']+".jpg", "wb")
    f.write(picture.content)
    f.close()