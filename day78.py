from flask import Flask

reflections = {
  "77":"Today we did some Flask",
  "78":"Today we did these reflections"
}

app = Flask(__name__)

@app.route('/<pageNumber>')

def index(pageNumber):
  f = open("template/reflections.html")
  page = f.read()
  f.close

  page = page.replace("{pageNumber}",pageNumber)
  page = page.replace("{bodyText}",reflections[pageNumber])

  return page

app.run(host='0.0.0.0', port=81)