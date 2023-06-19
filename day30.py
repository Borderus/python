# Exercise 1
#name = "Katie"
#age = "28"
#pronouns = "she/her"

#print("This is {}, using {} pronouns, and is {} years old.".format(name, pronouns, age))

#Exercise 2
#name = "Katie"
#age = "28"
#pronouns = "she/her"

#response = "This is {name}, using {pronouns} pronouns, and is {age} years old. Hello {name}. How are you? Have you been having a great {age} years so far?".format(name=name, pronouns=pronouns, age=age)

#print(response)

#Exercise 3

#name = "Katie"
#age = 28
#pronouns = "she/her"

#response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello {name}. How are you? Have you been having a great {age} years so far?"

#print(response)

#Exercise 4 - Alignment
# < left, ^ centre, > right

#for i in range(1,31):
#  print(f"Day {i:>2}: of 30")

#Fix my Code

#food = "pizza"
#location = "beach"
#color = "green"
#friend = "Quinn"

#response = "Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame.".format(food=food, location=location, color=color, friend=friend)

#print(response)

# Day 30 Challenge
length = 30

print(f"{length} days down")

for i in range(1,length+1):
  print(f"\nDay {i}:")
  response = input()
  
  restate = f"You thought Day {i} was {response}"
  
  print(f"{restate:^40}")