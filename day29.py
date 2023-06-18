# Exercise 1 - end= option
#Adding commas
#for i in range(0, 100):
#  print(i, end=", ")

#Adding new lines
#for i in range(0, 100):
#  print(i, end="\n")

#Adding tabs
#for i in range(0, 100):
#  print(i, end="\t")

#Adding vertical tabs
#for i in range(0, 100):
#  print(i, end="\v")

#Changing colours with the end = option
#print("If you put")
#print("\033[33m", end="") #yellow
#print("nothing as the")
#print("\033[35m", end="") #purple
#print("end character")
#print("\033[32m", end="") #green
#print("then you don't")
#print("\033[0m", end="") #default
#print("get odd gaps")
#N.B. COME BACK AND LOOK AT THIS ONE

#Using sep= option instead
#print("\nIf you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")

#Turning cursor on and off

#import os, time
#Off
#print('\033[?25l', end="")
#On
#print('\033[?25h', end="")
#for i in range(1, 31):
#  print(i)
#  time.sleep(0.2)
#  os.system("clear")
#input("Is the cursor on? ")

#-----------------------------------------------
#ANSI ESCAPE CODES
# Text Colour Code | Style Code | Text Bground Code
# Black         30 | None     0 | Black          30 
# Red           31 | Bold     1 | Red            31 
# Green         32 | Uline    2 | Green          32 
# Yellow        33 | Neg1     3 | Yellow         33 
# Blue          34 | Neg2     5 | Blue           34 
# Purple        35 |            | Purple         35 
# Cyan          36 |            | Cyan           36 
# White         37 |            | White          37 
# Default       39 |            | Default        39
#-----------------------------------------------

#Day 29 Challenge
#A subroutine to alter text colour

def textColour(word, colour):
  if colour.lower() == "black":
    print("\033[30m", end='')
    print(word, sep='', end=' ')
  elif colour.lower() == "red":
    print("\033[31m", end='')
    print(word, sep='', end=' ')
  elif colour.lower() == "green":
    print("\033[32m", end='')
    print(word, sep='', end=' ')
  elif colour.lower() == "yellow":
    print("\033[33m", end='')
    print(word, sep='', end=' ')
  elif colour.lower() == "blue":
    print("\033[34m", end='')
    print(word, sep='', end=' ')
  elif colour.lower() == "purple":
    print("\033[35m", end='')
    print(word, sep='', end=' ')
  elif colour.lower() == "cyan":
    print("\033[36m", end='')
    print(word, sep='', end=' ')
  elif colour.lower() == "white":
    print("\033[37m", end='')
    print(word, sep='', end=' ')    
  else:
    print(word, sep='', end=' ')

textColour("word", "")
textColour("word", "black")
textColour("word", "red")
textColour("word", "green")
textColour("word", "yellow")
textColour("word", "blue")
textColour("word", "purple")
textColour("word", "cyan")
textColour("word", "white")

print("")

textColour("Super Subroutine\n\nWith my","yellow")
textColour("new program", "purple")
textColour('I can just call textColour("and","red")', "yellow")
textColour("and","red")
textColour("that word will appear in the colour that I set it to.","yellow")
textColour("\n\nWith no","yellow")
textColour("weird gaps.","blue")
textColour("\n\nEpic.","yellow")