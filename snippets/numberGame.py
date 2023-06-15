#Day 18 Challenge

#Import packages
import datetime

# Pick target number - work under assumption that microseconds of time is uniformly random
now = str(datetime.datetime.now())
target = int(now[20:])

# Initialise
counter = 1

#Ask user to input numbers
print("I'm thinking of a number between 0 and 1,000,000...")
print("See if you can guess what number I'm thinking of - type your guess below!")

#Begin loop
while True:
  guess = int(input("> "))
  # Guessing logic
  if guess > target:
    print("Too high!")
  elif guess < 0:
    print("That's a negative number!")
    exit()
  elif guess < target:
    print("Too low!")
  elif guess == target:
    break
  else:
    print("That is not a number I recognise")
  # Increment counter
  counter += 1

#WInner message
print("You win! And only in "+str(counter)+" guesses!")