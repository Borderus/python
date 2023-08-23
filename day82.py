from flask import Flask, request

app = Flask(__name__)


@app.route('/language', methods=["GET"])
def language():
  get=request.args
  if "lang" not in get.keys():
    return "Data missing"
  else:
    langcode = get["lang"].lower()[0:3]
    if langcode in ["spa", "fra", "deu"]:
      f = open("template/page_"+langcode+".html")
      page = f.read()
      f.close()
      return page
    else:
      f = open("template/page_eng.html")
      page = f.read()
      f.close()
      return page

@app.route('/')
def index():
      return ''

app.run(host='0.0.0.0', port=81)