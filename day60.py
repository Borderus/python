import datetime

#Dev inputted date
#myDate = datetime.date(year=2022, month=12, day=7)
#print(myDate)

#Today's date
#today = datetime.date.today()
#print(today)

#User inputted date
#day = int(input("Day: "))
#month = int(input("Month: "))
#year = int(input("Year: "))

#date = datetime.date(year, month, day)
#print(date)

#Using a time delta to add two weeks onto a date
#today = datetime.date.today()

#difference = datetime.timedelta(days=14)

#newDate = today + difference
#print(newDate)

# Logical comparison
#today = datetime.date.today() # Today's date

#holiday = datetime.date(year = 2023, month = 7, day = 12) # The date of my holiday

#if holiday > today: # If my holiday is in the future
#  print("Coming soon")
#elif holiday < today: #If my holiday date has passed
#  print("Hope you enjoyed it")
#else: # If my holiday date is today
#  print("HOLIDAY TIME!")

#Fix my Code
#today = datetime.date.today() 

#holiday = datetime.date(year = 2022, month=7, day = 20) 

#if holiday < today: 
#  print("Coming soon")
#elif holiday > today: 
#  print("Hope you enjoyed it")
#else:
#  print("HOLIDAY TIME!")

today = datetime.date.today()

event = input("Input the event > ")

year = int(input("Input the year > "))
month = int(input("Input the month > "))
day = int(input("Input the day > "))

eventdate = datetime.date(year = year, month = month, day = day)
datediff = (eventdate - today).days

if datediff > 0:
  print(f"{event} is {datediff} days away!")
elif datediff < 0:
  print(f"{event} happened {abs(datediff)} days ago :(")
else:
  print(f"{event} is today!")