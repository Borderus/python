#Day 23 Challenge

#Define subroutine
def loginSystem():
  
  trueUser = "Stevo"
  truePW = "Coopdogg123"
  
  print("Replit Login System\n")

  while True:
    username = input("What is your username? ")
    password = input("What is your password? ")

    if (username==trueUser) and (password==truePW):
      print("Welcome to Replit!")
      break
    else:
      print("Error: Username or password not recognised.\n")

loginSystem()