#Exercise 1

#def reverse(value):
#  if value <= 0:
#    print("Done!")
#    return

#  else:
#    for i in range(value):
#      print("#", end="")
#    print()
#    reverse(value - 2)

#reverse(15)

#Day 57 Challenge
def factorial(value):
  if value > 0:
    if value == 1:
      return value
    else:
      return (value*(factorial(value-1)))

print(factorial(10))