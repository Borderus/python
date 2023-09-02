from flask import Flask, request, redirect
from replit import db
app = Flask(__name__, static_url_path='/static')

@app.route('/login')
def login():
  f = open("login.html", "r")
  page = f.read()
  f.close

  return page

@app.route('/logincheck', methods=['POST'])
def logincheck():
  global user
  form = request.form
  user = str(form["username"])
  try:
    if db[form["username"]]["password"] == form["password"]:
      return redirect("/yup")
    else:
      return redirect("/nope")
  except:
    return redirect("/nope")

@app.route("/yup")
def yup():
  page = "Hello "+user.title()
  return page

@app.route("/register")
def register():
  f = open("register.html", "r")
  page = f.read()
  f.close

  return page

@app.route("/addUser", methods=["POST"])
def addUser():
  form=request.form
  print(form)
  db[form["username"]]={"password":form["newPassword"]}
  return redirect("/login")

@app.route("/nope")
def nope():
  return redirect("/login")

@app.route('/')
def index():
  f = open("choose.html", "r")
  page = f.read()
  f.close

  return page

app.run(host='0.0.0.0', port=81)