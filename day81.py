from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/process', methods=["POST"])
def process():
  form = request.form
  if form["useranswer"] == form["answer"]:
    return "Welcome fellow robot"
  else:
    return "Begone slimy human"

@app.route('/')
def index():
  f = open("template/mainpage.html")
  page = f.read()
  f.close()

  answer=random.randint(1000, 999999)
  print(answer)

  page = page.replace("{ANSWER}", str(answer))
  page = page.replace("{ANSWERSQ}", str(answer**2))
  return page

app.run(host='0.0.0.0', port=81)