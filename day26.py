import os, time

#Exercise 1
#print("Welcome")
#print("to")
#print("Replit")

#time.sleep(1)
#os.system("clear")

#Day 26 Challenge
from replit import audio
def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    os.system("clear")    
    # Start taking user input and doing something with it
    userInput2 = input("Enter 1 to play\nEnter 2 to pause\nEnter 3 to exit\n\n")

    if userInput2 == "1":
      source.paused = False
    elif userInput2 == "2":
      source.paused = True
    elif userInput2 == "3":
      source.paused = True
      return
while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("MyPOD music player")
  time.sleep(1)
  print("")
  print("Enter 1 to play")
  time.sleep(1)
  print("Enter 2 to exit")
  print("")
  # take user's input
  userInput = input("")
  # check whether you should call the play() subroutine depending on user's input
  if userInput.lower() == "1":
    os.system("clear")    
    play()
  elif userInput.lower() == "2":
    break