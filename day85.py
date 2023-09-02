from flask import Flask, request, redirect, session
from replit import db
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key=os.environ['sessionKey']

@app.route('/')
def index():
  session.clear()
  session["logged_in"] = False
  f = open("choose.html", "r")
  page = f.read()
  f.close
  return page

@app.route('/login')
def login():
  session["logged_in"] = False
  f = open("login.html", "r")
  page = f.read()
  f.close
  return page

@app.route('/logincheck', methods=['POST'])
def logincheck():
  form = request.form
  try:
    if db[form["username"]]["password"] == form["password"]:
      session["user"] = form["username"]
      session["logged_in"] = True
      return redirect("/yup")
    else:
      return redirect("/nope")
  except KeyError:
    return redirect("/nope")

@app.route("/yup")
def yup():
  print(session["logged_in"])
  if session["logged_in"] == True:
    page = "Hello "+session["user"]
    return page
  else:
    return redirect("/")

@app.route("/nope")
def nope():
  return redirect("/login")

@app.route("/register")
def register():
  f = open("register.html", "r")
  page = f.read()
  f.close
  return page

@app.route("/addUser", methods=["POST"])
def addUser():
  form=request.form
  db[form["username"]]={"password":form["newPassword"]}
  print(db.keys())
  return redirect("/login")

app.run(host='0.0.0.0', port=81)