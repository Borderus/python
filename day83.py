from flask import Flask, redirect, request

app = Flask(__name__)

def createEntry(title, date, text):
  page = ""
  f = open("template/blogEntry.html", "r")
  page = f.read()
  f.close()
  
  page = page.replace("{title}", title)
  page = page.replace("{date}", date)
  page = page.replace("{text}", text)
  return page
  
@app.route('/')
def index():
  return redirect('home/')
  
@app.route('/home/', methods=["GET"])
def home():
  page = ""
  f = open("template/menu.html", "r")
  page = f.read()
  f.close()
  get=request.args
  if "style" not in get.keys():
    page = page.replace("{STYLE}", "blogEntry")
  else:
    page = page.replace("{STYLE}", get["style"])
  return page

@app.route('/home/2023-10-25/')
def home20230125():
  return redirect('/2023-10-25/')

@app.route('/2023-10-25/')
def entry01():
  title = "My brand new blog"
  date = "October 25th 2023"
  text = "Here is my first blog entry."
  return createEntry(title, date, text)

@app.route('/home/2023-10-26/')
def home20230126():
  return redirect('/2023-10-26/')

@app.route('/2023-10-26/')
def entry02():
  title = "Bored of this"
  date = "October 26th 2023"
  text = "It's been like, two whole days and I'm just sick of this. Sayonara suckers."
  return createEntry(title, date, text)
 
app.run(host='0.0.0.0', port=81)