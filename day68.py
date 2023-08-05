#Initialise
import tkinter as tk

dictPics = {}

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x350") 

#Subroutines
def changeImage():
  imageNotFound.pack_forget()
  canvas.pack_forget()
  search = textbox.get().lower().strip()
  found = False
  for item, value in dictPics.items():
    if search == item:
      canvas.pack()
      canvas.itemconfig(container, image = value) 
      found = True
  if found == False:
    imageNotFound.pack()

def createPic(name):
  fname = name.title()+".png"
  output = tk.PhotoImage(file=fname)
  dictPics[name.lower()] = output
  return output

#Define
hello = tk.Label(text = "Guess Who?") 
imageNotFound = tk.Label(text="Unable to find this user")

textbox = tk.Entry()

canvas = tk.Canvas(window, width = 300, height=300)

charlotte = createPic("charlotte")
gerald = createPic("gerald")
katie = createPic("katie")
mo = createPic("mo")
ugluk = createPic("ugluk")

container = canvas.create_image(150,150)

button = tk.Button(text = "Click me!", command=changeImage)

#Pack
hello.pack()
textbox.pack()
button.pack()
canvas.pack()

#Main loop
tk.mainloop()