#Exercise 1

#myString = "Day 38"
#for letter in myString:
#  print(letter)

#Exercise 2

#myString = "Will my vowels be yellow?"
#vowels = ['a', 'e', 'i', 'o', 'u']

#for letter in myString:
#  if letter.lower() in vowels:
#    print('\033[33m', end='')
#    print(letter, end='')
#    print('\033[39m', end='')
#  else:
#    print(letter, end='')

# ------------ Day 38 Challenge ------------

#Set up relevant lists
colours = ['r','g','y','b','p', ' ']
colourCodes = ['\033[31m','\033[92m','\033[33m','\033[94m','\033[95m','\033[39m']

#Get user input
print("\033[33mWhat sentence do you want rainbow-ising?\033[39m")
sentence = input('\033[92m')
print('\033[39m', end='')

#Establish subroutine to change colours
def changeColour(letter):
  for count in range(0, len(colours)):
    if letter.lower() == colours[count]:
      print(colourCodes[count], end='')

#Print sentence
for letter in sentence:
  changeColour(letter)
  print(letter, end='')