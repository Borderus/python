#--Import packages, initialise lists and variables--

#Import packages
import os, time, random, sys

#Number of guesses
NoOfGuesses = 6

#Get words, create lists for correct and incorrect guesses
listOfWords = []
correctGuesses = []
incorrectGuesses = []

with open("wordlist.txt") as file:
  for line in file:
    line = line.strip().upper()
    listOfWords.append(line)
    
#listOfWords = ["Mississippi"]
answer = random.choice(listOfWords)

#List of pictures of the hangman in ASCII art
hangmanpics = ['''
                 +---+
                 |   |
                     |
                     |
                     |
                     |
               =========''', '''
                 +---+
                 |   |
                 O   |
                     |
                     |
                     |
               =========''', '''
                 +---+
                 |   |
                 O   |
                 |   |
                     |
                     |
               =========''', '''
                 +---+
                 |   |
                 O   |
                /|   |
                     |
                     |
               =========''', '''
                 +---+
                 |   |
                 O   |
                /|\  |
                     |
                     |
               =========''', '''
                 +---+
                 |   |
                 O   |
                /|\  |
                /    |
                     |
               =========''', '''
                 +---+
                 |   |
                 O   |
                /|\  |
                / \  |
                     |
               =========''']

#------------Subroutine to print centre------------
def cprint(userString):
  print(f"{userString:^40}")



def printGuesses():
  showString = ""
  for letter in answer:
    if letter in correctGuesses:
      showString = showString + " \033[4m" + letter + "\033[24m "
    else:
      showString = showString + " " + "_" + " "
  #Print letters
  spaceString = ""
  spaceStringLen = (40 - 3*len(answer))//2
  for i in range(spaceStringLen):
    spaceString = spaceString + " "
  print(spaceString, end='')
  print(showString)  

#------------Subroutine to print screen-------------
def printGameScreen():
  os.system("clear")
  print()
  print(hangmanpics[len(incorrectGuesses)])
  print()
  printGuesses()
  print()
  #Incorrect letters
  print("Incorrect guesses: ", end = '')
  counter = 1
  for letter in incorrectGuesses:
    print(letter, end='')
    if counter != len(incorrectGuesses):
      print(", ", end='')
    counter += 1
  print()
  
  #User input
  guess = input("Enter your letter: ").upper().strip()

  #Exit if requested
  if guess == "EXIT":
    sys.exit()
    
  #Return value of guess to subroutine
  return guess

#------------Subroutine to print title-------------
def printTitleScreen():
  os.system("clear")
  cprint("Hangman")
  print(hangmanpics[0])
  print()
  cprint("Press enter to begin")
  input()

#----------Subroutine to print winscreen------------
def printWinScreen(wincount):
  os.system("clear")
  cprint("YOU WIN!")
  print(hangmanpics[len(incorrectGuesses)])
  print()
  printGuesses()
  input()
  sys.exit()

#----------Subroutine to print gameover------------
def printLoseScreen(answer):
  os.system("clear")
  cprint("GAME OVER")
  print(hangmanpics[6])
  print()
  printGuesses()
  print()
  cprint("YOU LOSE!")
  cprint("THE ANSWER WAS "+answer)  
  input()
  sys.exit()

#----------Subroutine for guessing logic------------
def playerGuess(guess):
  correct = 0
  wincount = 0
  for letter in answer:
    if guess == letter:
      cprint("Correct guess")
      correct = 1
      correctGuesses.append(guess)
    if letter in correctGuesses:
      wincount += 1
  if correct == 0:
    cprint("Incorrect guess")
    incorrectGuesses.append(guess) 
  return wincount

def winLose(wincount, answer):
    #Win/lose logic
  if wincount == len(answer):
    printWinScreen(wincount)
  if len(incorrectGuesses) == NoOfGuesses:
    printLoseScreen(answer)

#---------------------Test vars--------------------
def showVars():
  print(answer)
  print(wincount)
  print(len(incorrectGuesses))
  print(correctGuesses)
  print(incorrectGuesses)
  time.sleep(1)
#---------------------Run Game---------------------

printTitleScreen()
while True:
  guess = printGameScreen()
  wincount = playerGuess(guess)
  winLose(wincount, answer)
  
  #showVars()

