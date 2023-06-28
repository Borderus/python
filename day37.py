#Exercise 1

#myString = "How's it going?"
#print(myString[0])

#Exercise 2

#We can do the first 4 chars
#print(myString[0:4])
#Or th rest
#print(myString[4:15])
#Missing the first index defaults it to 0
#print(myString[:7])
#Leaving the last blank defaults it to the end
#print(myString[7:])
#We can even print every other letter
#print(myString[0:15:2])
#Or using some shorthand to do every third letter
#print(myString[::3])
#Or with negative numbers we can go backwards
#print(myString[::-1])

#Exercise 3
#The split() function breaks up a string into a list
#myString2 = "Hello there my friend"
#print(myString2.split())

#Fix My Code
#myString3 = "Hello there my friend."
#print(myString3[0:11:1])

#Day 37 Challenge

import os, time

forename = input("What is your first name? ")
surname = input("And what is your surname? ")
swForename = forename[:3].title()+surname[:3].title()

mother = input("And what was your mother's name? ")
team = input("And which football team do you support? ")
swSurname = mother[:2].title()+team[len(team)-3:].title()

os.system("clear")
print(f"Your Star Wars name is {swForename} {swSurname}")
time.sleep(0.8)