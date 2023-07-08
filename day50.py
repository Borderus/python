#------------------Initialise------------------
import os, time, random
ideaList = []
filename = "idea_list.txt"

#-------------If file doesn't exist------------
if not os.path.exists(filename):
  f = open(filename, "x")
  f.close()
  print("Creating idea list...")
  time.sleep(0.7)
  os.system("clear")

#------------------WRITELIST-------------------
def writeList(idea):
    f = open(filename, "a+")
    f.write("\n"+idea)
    f.close()
    print("> Adding idea to list...")
    time.sleep(0.2)
    print("> Idea added successfully")

#-------------------READLIST-------------------
def readList():
  f = open(filename, "r")
  ideaList = f.read().split("\n")
  f.close()

  randIdea = ideaList[random.randint(0,len(ideaList)-1)]
  print(f">\n>{randIdea:^48}")
  time.sleep(0.5)

#-------------------RUN CODE-------------------
while True:
  print(f"{'Idea Manager':^50}")
  
  menu = input("\nAdd an idea, see a random idea or quit? a/r/q\n\n> ")
  
  if menu.lower().split()[0] == "a":
    writeList(input("> What would you like to add?\n> "))
  if menu.lower().split()[0] == "r":
    readList()
  if menu.lower().split()[0] == "q":
    break

  time.sleep(1)
  os.system("clear")