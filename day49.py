#Exercise 1

#f = open("high.score", "r")
#contents = f.read()
#f.close()

#contents = contents.split()
#print(contents)

#Exercise 2

#f = open("high.score", "r")
#contents = f.readline()
#f.close()

#print(contents)

#Exercise 3

#f = open("high.score")
#while True:
#  contents = f.readline().strip()
#  if contents == "":
#    break
#  print(contents)
#f.close()

#Fix My Code
#f = open("high.score","r")

#while True:
#  contents = f.readline().strip()
#  if contents == "":
#    break
#  print(contents)

#f.close()

#Day 49 Challenge
#Initialise
winPlayer = ""
winScore = 0

#Read in
f = open("high.score", "r")
contents = f.read().split("\n")
f.close()

for line in contents:
  data = line.split()
  if data != []:
    if int(data[1]) > winScore:
      winPlayer = data[0]
      winScore = int(data[1])

#Print winner
print(f"Current leader is {winPlayer}")
print(f"{winScore}")