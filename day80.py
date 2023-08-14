from flask import Flask, request, redirect
import random

succSalt = str(random.randint(100000, 999999))

def getPage(URL):
  f = open(URL)
  page = f.read()
  f.close()
  return page

app = Flask(__name__)

@app.route('/process', methods=["POST"])
def process():
  form = request.form
  if form["username"] == "Ben" and form["password"] == "AvocadoConstant":
    return redirect('/'+succSalt)
  else:
    return redirect('/splash')

@app.route('/')
def index():
  return getPage("template/login.html")

@app.route('/'+succSalt)
def success():
  return getPage("template/success.html")

@app.route('/splash')
def splash():
  return getPage("template/splash.html")

app.run(host='0.0.0.0', port=81)