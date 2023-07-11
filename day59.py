#Day 59 Challenge
#def palindrome(word):
#  palindrome = True

#  for counter in range(len(word)):
#    if word[counter] != word[len(word) - counter - 1]:
#      palindrome = False

#  print(palindrome)

#word = input("What would you like to test for palindrome-hood? ").replace(" ","").lower()
#palindrome(word)

def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])
print(palindrome("lemon"))