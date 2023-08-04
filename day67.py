import tkinter as tk

dictPics = {}

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x350") 

def changeImage():
  search = textbox.get().lower().strip()
  for item, value in dictPics.items():
    if search == item:
      canvas.itemconfig(container, image = value) 

def createPic(name):
  fname = name.title()+".png"
  output = tk.PhotoImage(file=fname)
  dictPics[name.lower()] = output
  return output

hello = tk.Label(text = "Guess Who?") 

textbox = tk.Entry()

canvas = tk.Canvas(window, width = 300, height=300)

charlotte = createPic("charlotte")
gerald = createPic("gerald")
katie = createPic("katie")
mo = createPic("mo")
ugluk = createPic("ugluk")

container = canvas.create_image(150,150)

button = tk.Button(text = "Click me!", command=changeImage)

hello.pack()
textbox.pack()
button.pack()
canvas.pack()

tk.mainloop()