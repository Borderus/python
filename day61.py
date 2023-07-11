#Exercise 1
#from replit import db

#db["david"] = {"username":"dmorgan", "password": "baldy1"}
#db["danny"] = {"username":"dmorgan", "password": "danny1"}

#keys = db.keys()
#for key in keys:
#  print(f"""{key}: {db[key]}""")

#Fix My Code

#try:
#  value = db["key"]
#except KeyError:
#  pass

#keys = db.keys()
#for key in keys:
#  print(key)


#Day 56 Challenge
from replit import db
import os, time, datetime

#-----------------------------Read in tweetlist----------------------------------
def readIn():
  tweetList = []
  keys=db.keys()
  for key in keys:
    tweetList.append(key)
  tweetList.sort(reverse=True)
  return tweetList

#------------------------------Add to tweetlist----------------------------------
def addTweet():
  tweet = input("Tweet: ")
  timestamp = datetime.datetime.now()
  db[timestamp] = {"tweet": tweet}
  time.sleep(0.7)
  print("Sent!")
  time.sleep(0.7)

#-------------------------------View tweetlist-----------------------------------
def viewTweets():
  start = 0
  increment=10

  print(f"{'TWEETS':^40}")
  while True:
    try:
      for counter in range(start,start+increment):
        print(f"{tweetList[counter][0:16]:<40}")
        print(f"{db[tweetList[counter]]['tweet']:>40}\n")
        time.sleep(0.5)
    except IndexError:
      time.sleep(0.5)
      input("No more Tweets - press enter to return to menu...")
      break
    time.sleep(0.5)
    seeMore = input("\nSee more Tweets? ").strip().lower()[0]
    if seeMore == "n":
      break
    start += increment
    print()

#----------------------------------RUN CODE--------------------------------------
while True:
  os.system("clear")
  tweetList = readIn()
  menu = input("Add or view tweets? ")
  os.system("clear")
  time.sleep(0.5)
  if menu.strip().lower()[0] == "a":
    addTweet()
  elif menu.strip().lower()[0] == "v":
    viewTweets()
  elif menu.strip().lower()[0] == "q":
    break