def textColour(word, colour):
  if colour.lower() == "black":
    return "\033[30m"+word
  elif colour.lower() == "red":
    return "\033[31m"+word
  elif colour.lower() == "green":
    return "\033[32m"+word
  elif colour.lower() == "yellow":
    return "\033[33m"+word
  elif colour.lower() == "blue":
    return "\033[34m"+word
  elif colour.lower() == "purple":
    return "\033[35m"+word
  elif colour.lower() == "cyan":
    return "\033[36m"+word
  elif colour.lower() == "white":
    return "\033[37m"+word  
  else:
    return "\033[39m"+word

def indent(counter):
  indent = ""
  for i in range(counter):
    indent = indent+" "
  return indent

title = textColour("=","red")+textColour("=","white")+textColour("=","blue")+textColour(" Music App ","yellow")+textColour("=","blue")+textColour("=","white")+textColour("=","red")
track = textColour("Radio Gaga","white")
artist = textColour("Queen","yellow")
prev = textColour("PREV","white")
next = textColour("NEXT", "green")
pause = textColour("PAUSE", "purple")

print(f"{title:>70}\n")

print(indent(7)+f"{track}")
print(indent(7)+f"{artist}\n")

print(f"{prev:<23}")
print(f"{next:^23}")
print(f"{pause:>24}")

print()
print()
print()

title2_1 = textColour("WELCOME  TO", "white")
title2_2 = textColour("--     ARMBOOK     --", "blue")
body2_1 = textColour("Definitely not a rip off of", "yellow")
body2_2 = textColour("a certain other social", "yellow")
body2_3 = textColour("networking site.", "yellow")
body2_4 = textColour("Honest.", "red")
body2_5 = textColour("Username: ", "white")
body2_6 = textColour("Password: ", "white")

print(indent(15)+f"{title2_1:^26}")
print(indent(15)+title2_2+"\n")

print(indent(15)+f"{body2_1:>32}")
print(indent(15)+f"{body2_2:>32}")
print(indent(15)+f"{body2_3:>32}"+"\n")

print(indent(15)+f"{body2_4:^26}"+"\n")
username = input(indent(15)+f"{body2_5:>21}")
password = input(indent(15)+f"{body2_6:>21}")