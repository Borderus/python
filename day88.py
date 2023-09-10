#*********************************
#             SETUP              *
#*********************************

import os
from replit import db
from flask import Flask, redirect, request, session
app = Flask(__name__, static_url_path='/static')
app.secret_key=os.environ['sessionKey']

#*****REDIRECT ROOT TO BLOG*******
@app.route('/')
def index():
  return redirect('/blog')

#*********************************
#            LOGIN               *
#*********************************

@app.route('/login', methods=['POST'])
def login():
  f = open('static/pages/login.html')
  page = f.read()
  f.close()
  return page

#************LOGOUT***************
@app.route('/logout')
def logout():
  session.clear()
  session["logged_in"] = False
  return redirect("/blog")
    
#*********************************
#             BLOG               *
#*********************************

@app.route('/blog')
def blog():
  #---------LOGIN BUTTON----------
  def loginButton():
    button = ""
    f = open("static/pages/login_button.html", "r")
    button = f.read()
    f.close()
    return button
  #----------NEW ENTRY-----------
  def newEntry():
    form = ""
    f = open("static/pages/newEntry.html", "r")
    form = f.read()
    f.close()
    return form
  #----------ENTRY FORM-----------
  def entryForm():
    try:
      if request.headers["X-Replit-User-Name"]=="benback96":
        return newEntry()
      else:
        return loginButton()
    except KeyError:
      return loginButton()
  #-----------ENTRIES-------------
  def entries():
    entries = "<hr>"
    keys = db.keys()
    for key in reversed(sorted(keys)):
      f = open("static/pages/entry.html", "r")
      entry = f.read()
      f.close()
      entry = entry.replace("{DATE}", key)
      entry = entry.replace("{TITLE}", db[key]["title"])
      entry = entry.replace("{ENTRY}", db[key]["entry"])
      entries += entry
    return entries
  #-------------BLOG--------------
  f = open("static/pages/blog.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{ENTRYFORM}", entryForm())
  page = page.replace("{ENTRIES}", entries())
  return page

#**************BLOG***************
@app.route("/postEntry", methods=['POST'])
def updateBlog():
    try:
      if session["logged_in"] == True:
        form = request.form
        db[form["date"]] = {"title": form["title"], "date": form["date"], "entry": form["paragraph_text"]}
        return redirect('/blog')
      else:
        return redirect('/blog')
    except KeyError:
      return redirect('/blog')
  

app.run(host='0.0.0.0', port=81)
