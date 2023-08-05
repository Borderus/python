                      #Initialise
import tkinter as tk

window = tk.Tk()
window.title("Visual Novel")
window.geometry("480x405")

#Subroutines
def forgetAll():
  button01.pack_forget()
  label11.pack_forget()
  button11.pack_forget()
  button12.pack_forget()
  label21.pack_forget()
  button21.pack_forget()
  label31.pack_forget()
  button31.pack_forget()
  button32.pack_forget()  
  label41.pack_forget()
  label42.pack_forget()
  label51.pack_forget()
  button51.pack_forget()
  label61.pack_forget()
  button61.pack_forget()
  button62.pack_forget()
  label71.pack_forget()
  label72.pack_forget()
  label81.pack_forget()
  label82.pack_forget()

def button01Click():
  forgetAll()
  canvas01.itemconfig(container, image=image11)
  label11.pack()
  button11.pack()
  button12.pack()  

def button11Click():
  forgetAll()
  canvas01.itemconfig(container, image=image21)
  label21.pack()
  button21.pack()

def button21Click():
  forgetAll()
  canvas01.itemconfig(container, image=image31)
  label31.pack()
  button31.pack()
  button32.pack()

def button31Click():
  forgetAll()
  canvas01.itemconfig(container, image=image41)
  label41.pack()
  label42.pack()
  button01.pack()

def button12Click():
  forgetAll()
  canvas01.itemconfig(container, image=image51)
  label51.pack()
  button51.pack()

def button51Click(): 
  forgetAll()
  canvas01.itemconfig(container, image=image61)
  label61.pack()
  button61.pack()
  button62.pack()

def button61Click():
  forgetAll()
  canvas01.itemconfig(container, image=image71)
  label71.pack()
  label72.pack()
  button01.pack()

def button62Click():
  forgetAll()
  canvas01.itemconfig(container, image=image81)
  label81.pack()
  label82.pack()

                        #Define
#Global Assets
label01 = tk.Label()
canvas01 = tk.Canvas(window, width = 400, height = 300)
button01 = tk.Button(text = "Try again!", width = 24, command=button01Click)

#Page 1
image11 = tk.PhotoImage(file = "Day67/Snrub1.png").subsample(2)
label11 = tk.Label(text="Hello there! My name is...")
button11 = tk.Button(text = "Mr Burns!", width = 12, command=button11Click)
button12 = tk.Button(text = "Mr... Snrub!", width = 12, command=button12Click)

#Page 2
image21 = tk.PhotoImage(file = "Day67/Snrub1.png").subsample(2)
label21 = tk.Label(text="The crowd mutters amongst themselves...")
button21 = tk.Button(text = "Keep talking!", width = 12, command=button21Click)

#Page 3
image31 = tk.PhotoImage(file = "Day67/Snrub2.png").subsample(2)
label31 = tk.Label(text="And I come from some place...")
button31 = tk.Button(text = "Where we can marry our cousins!", width = 24, command=button31Click)
button32 = tk.Button(text = "Far away!", width = 24, command=button31Click)

#Page 4
image41 = tk.PhotoImage(file = "Day67/Snrub3.png").subsample(2)
label41 = tk.Label(text="The crowd are onto you! Cries of Boo-urns come ")
label42 = tk.Label(text="from the stands and you have to make a quick escape!")

#Page 5
image51 = tk.PhotoImage(file = "Day67/Snrub1.png").subsample(2)
label51 = tk.Label(text="The fools seem to be falling for it...")
button51 = tk.Button(text = "Keep talking!", width = 12, command=button51Click)

#Page 6
image61 = tk.PhotoImage(file = "Day67/Snrub2.png").subsample(2)
label61 = tk.Label(text="And I come from some place...")
button61 = tk.Button(text = "Where we can marry our cousins!", width = 24, command=button61Click)
button62 = tk.Button(text = "Far away!", width = 24, command=button62Click)

#Page 7
image71 = tk.PhotoImage(file = "Day67/Snrub3.png").subsample(2)
label71 = tk.Label(text="Zounds! The crowd turns on you,")
label72 = tk.Label(text="yelling something about lemons!")

#Page 8
image81 = tk.PhotoImage(file = "Day67/Snrub4.png").subsample(2)
label81 = tk.Label(text="")
label82 = tk.Label(text="Yes, that will do!")

#Container
container = canvas01.create_image(200,150, image=image11)

                          #Pack
label01.pack()
canvas01.pack()

label11.pack()
button11.pack()
button12.pack()

                         #Mainloop
tk.mainloop()