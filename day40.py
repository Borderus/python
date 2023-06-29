#Exercise 1

#Dictionaries are lists composed of key-value pairs

#myUser = {"name":"David", "age":128}

#print(myUser["name"])

#myUser["name"] = "The legendary David"
#print(myUser)

#Fix My Code
#myUser = {"name":"Andy", "age": 129}
#print(myUser["name"])

print(f'{"Contact Card":^40}')

contactCard = {}

print()
nameList = input("Input your name > ").split()
contactCard.update({"forename": nameList[0], "surname": nameList[len(nameList) - 1]})
print()
phoneNo = input("Input your phone number > ")
contactCard.update({"phoneNo": phoneNo})
print()
email = input("Input your email > ")
contactCard.update({"email":email})
print()
address = input("Input your address > ")
contactCard.update({"address":address})

print(f'Hi {contactCard["forename"]} {contactCard["surname"]}. Our dictionary says that we can call you on {contactCard["phoneNo"]}, email at {contactCard["email"]} or write to you at {contactCard["address"]}.')
