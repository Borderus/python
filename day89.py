from flask import Flask, request, redirect
from replit import db
import datetime

app = Flask(__name__)

@app.route('/')
def index():
  if request.headers['X-Replit-User-ID'] == '23197373':
    admin = True
  #Get template
  f = open('static/pages/mainpage.html', 'r')
  page = f.read()
  f.close()
  #Change variables
  page = page.replace('{USERNAME}', request.headers['X-Replit-User-Name'])
  #Cycle through entries and add
  entries = ''
  entryList = reversed(sorted(db.keys()))
  for key in entryList:
    value = db[key]
    entries += entry(key, value, admin)
  page = page.replace('{ENTRIES}', entries)
  #Return finished page
  return page

def entry(key, value, admin):
  #Get template
  f = open('static/pages/entry.html', 'r')
  page = f.read()
  f.close()
  #Get button
  f = open('static/pages/button.html', 'r')
  button = f.read()
  f.close()
  #Change variables
  page = page.replace('{USERNAME}', value['username']+' - '+value['date']+' '+value['time'])
  page = page.replace('{USERID}', value['userid'])
  page = page.replace('{ENTRY}', value['message'])
  if admin == True:
      page = page.replace('{BUTTON}', button)
  else:
    page = page.replace('{BUTTON}', '')
  page = page.replace('{KEY}', key)
  #Return finished page
  return page

#-------------------ADD POST------------------------
@app.route('/addpost', methods=['POST'])
def addpost():
  #Get entry key
  now = datetime.datetime.now()
  key = str(now)[0:19]
  key = key.replace(" ", "")
  key = key.replace("-", "")
  key = key.replace(":", "")
  key += request.headers['X-Replit-User-ID']
  #Input entry values
  form=request.form
  db[key] = {'userid': request.headers['X-Replit-User-ID'], 'username': request.headers['X-Replit-User-Name'], 'message': form["message"], 'date': now.strftime('%x'), 'time': now.strftime('%X')}

  return redirect('/')


@app.route('/delete', methods=['POST'])
def delete():
  #Input entry values
  form=request.form
  del db[form["Delete"]]

  return redirect('/')

app.run(host='0.0.0.0', port=81)