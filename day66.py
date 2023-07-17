#Exercise 1

#import tkinter as tk

#window = tk.Tk()
#window.title("Hello World")
#window.geometry("300x300")

#label = "Hello there world"
#label2 = 0

#def updateLabel():
#  global label2
  
#  label = "Bye World!"
#  hello["text"] = label

#  number = text.get("1.0", "end")
#  try:
#    number = int(number)
#    label2 += number
#    counter["text"] = label2
#  except ValueError:
#    pass

#hello = tk.Label(text = label)
#counter = tk.Label(text = label2)
#text = tk.Text(window, height=1, width=20)
#button = tk.Button(text = "Click Me!", command = updateLabel)
#button2 = tk.Button(text = "Another button", command = updateLabel)
#button3 = tk.Button(text = "Last one", command = updateLabel)

#hello.grid(row=0, column=1)
#counter.grid(row=1, column=1)
#text.grid(row=2, column=1)
#button.grid(row=3, column=0)
#button2.grid(row=3, column=1)
#button3.grid(row=3, column=2)

#tk.mainloop()

#Fix My Code

#window = tk.Tk()
#window.title("Hello World") 
#window.geometry("300x300") 

#label = 0

#def updateLabel():
#  global label
#  number = text.get("1.0","end") 
#  try:
#    number = int(number) 
#    label += number
#    hello["text"] = label
#  except ValueError:
#    print("Error: Not a number")
  

#hello = tk.Label(text = label)
#hello.grid(row=0, column=1)

#text = tk.Text(window ,height=1, width = 20)
#text.grid(row=1, column=1) # New line here

#button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

#button = tk.Button(text = "Another Button", command = updateLabel).grid(row=2, column=1)

#button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

#tk.mainloop()

#Day 66 - DOGULATOR

import tkinter as tk
#from replit import audio
#import time

window = tk.Tk()
window.title("Dogulator") 
window.geometry("400x400")

calcString = ""
label1 = tk.Label(text = calcString)

#answer = eval(calcString)
answer = 0
label2 = tk.Label(text = answer)

def keyStroke(key):
  global calcString, answer
  if calcString == "" and key in ["+","-","*","/"] != 0:
    calcString = str(answer)+key
  else:
    calcString = calcString + key
  label1["text"] = calcString
  label2["text"] = ""

def equals():
  global calcString, answer
  try:
    answer = eval(calcString)
    sum = calcString+"="
    calcString = ""
    label1["text"] = sum
    label2["text"] = answer
  except ValueError:
    print("Error: Not a valid sum")

button1 = tk.Button(text = "1", command = lambda: keyStroke("1"))
button2 = tk.Button(text = "2", command = lambda: keyStroke("2"))
button3 = tk.Button(text = "3", command = lambda: keyStroke("3"))
button4 = tk.Button(text = "4", command = lambda: keyStroke("4"))
button5 = tk.Button(text = "5", command = lambda: keyStroke("5"))
button6 = tk.Button(text = "6", command = lambda: keyStroke("6"))
button7 = tk.Button(text = "7", command = lambda: keyStroke("7"))
button8 = tk.Button(text = "8", command = lambda: keyStroke("8"))
button9 = tk.Button(text = "9", command = lambda: keyStroke("9"))
button0 = tk.Button(text = "0", command = lambda: keyStroke("0"))

buttonplus = tk.Button(text = "+", command = lambda: keyStroke("+"))
buttonminus = tk.Button(text = "-", command = lambda: keyStroke("-"))
buttonstar = tk.Button(text = "*", command = lambda: keyStroke("*"))
buttonslash = tk.Button(text = "/", command = lambda: keyStroke("/"))

buttonlbrack = tk.Button(text = "(", command = lambda: keyStroke("("))
buttonrbrack = tk.Button(text = ")", command = lambda: keyStroke(")"))

buttonequals = tk.Button(text = "=", command = equals)

label1.grid(row = 0, column = 0, columnspan = 5, sticky=tk.W)
label2.grid(row = 1, column = 0, columnspan = 5, sticky=tk.E)
button1.grid(row = 2, column = 0)
button2.grid(row = 2, column = 1)
button3.grid(row = 2, column = 2)
buttonplus.grid(row = 2, column = 3)
buttonminus.grid(row = 2, column = 4)
button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)
buttonstar.grid(row = 3, column = 3)
buttonslash.grid(row = 3, column = 4)
button7.grid(row = 4, column = 0)
button8.grid(row = 4, column = 1)
button9.grid(row = 4, column = 2)
buttonlbrack.grid(row = 4, column = 3)
buttonrbrack.grid(row = 4, column = 4)
button0.grid(row = 5, column = 1)
buttonequals.grid(row = 5, column = 3, columnspan = 2, sticky = tk.EW)

tk.mainloop()

#Make grid larger
#Add dog theming

#Code to play audio
#audio.play_file("o_fortuna.mp3")
#time.sleep(10)