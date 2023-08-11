from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    return """<html>
      <body>
        <p>
          <a href=/portfolio>
            Check out the Python portfolio!
          </a>
        </p>
        <p>
          <a href=/linktree>
            Or the stuff we've been doing with HTML!
          </a>
        </p>
      </body>
    </html>"""

@app.route('/linktree') # Creates the path to the linktree page
def linktree(): # Subroutine to create the linktree page
  page = f"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <h1>WHAT UP!!!</h1>
  <img src=static/images/The_Gang.jpg width = 50%>
  <p>We're three cool guys looking for other cool guys who want to hang out in our party mansion. Nothing sexual. Dudes in good shape encouraged. If you are fat you should be able to find the humour in the little things.</p>
  
  <p>Once again, nothing sexual.</p>
  <br/>
  <h2>About us</h2>
  <p>We're three regular dudes who work at Paddy's Pub here in the heart of South Philly! We also maintain a few other enterprises like Kitten Mittons, Fight Milk and DickTowel.com (see below).</p>
  <div class="row">
    <div class="column">
      <img class=enterprises src="static/images/Kitten_Mittens.png">
    </div>
    <div class="column">
      <img class=enterprises src="static/images/Fight_Milk.png">
    </div>
    <div class="column">
      <a href='https://www.dicktowel.com/'><img class=enterprises src="static/images/Dick_Towel.png"></a>
    </div>
  </div>

  <p>
    We also maintain a wide array of hobbies, such as sailing, attending bodybuilding shows and ghouls.
  </p>
  <p>
    So come down and join the party today! We're sure it'll be a home run!
  </p>
  <br/>
  <p class=ps>
    Once again, nothing sexual.
  </p>
  <br/>
  <p class=footer>
    {datetime.date.today()}
  </p>
</body>

</html>
"""
  return page
  
@app.route('/portfolio') # Creates the path to the portfolio page
def portfolio(): # Subroutine to create the portfolio page
  page = """<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href=Day74.css rel="stylesheet" type="text/css"/>
</head>

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>
      Ben's Python Projects
    </title>
    <link href=Day74.css rel="stylesheet" type="text/css"/>
  </head>

  <body>
    <h2>
      Ben's Favourite Python Projects
    </h2>

    <h3>
      Calculator
    </h3>
    <a href = https://replit.com/@benback96/Day66100Days><img src=static/images/Calculator.png width=70%>
    </a>
    <p>
      As part of the toe-dip into OOP, we built a calculator! This project was the first encounter with Lambda functions, though as the title at the top belies, there are further plans for this one.
    </p>

    <h3>
      Diary
    </h3>
    <a href = https://replit.com/@benback96/Day72100Days><img src=static/images/Diary.png width=70%>
    </a>
    <p>
      A super-secret diary! Complete with a hashed and salted password to keep out intruders, this project maintained the contents between sessions in ReplitDB.
    </p>

    <h3>
      Hangman
    </h3>
    <a href = https://replit.com/@benback96/Day39100Days><img src=static/images/Hangman.png width=70%>
    </a>
    <p>
      A classic! The children's game, brought to life on your screen. Actually easier than anticipated, once we'd sourced the ASCII art.
    </p>

    <h3>
      Mr Snrub's Choose Your Own Adventure
    </h3>
    <a href = https://replit.com/@benback96/Day69100Days><img src=static/images/Snrub.png width=70%>
    </a>
    <p>
      The highest rated episode of the Simpsons on IMDB is Marge vs. The Monorail, an utter classic. And now, you can relive it in all its glory as a Choose Your Own Adventure game!
    </p>
  <br>
  <br>
  </body>
</html>
"""
  # Three quotes - I'm going to write or paste my HTML code here. The HTML gets assigned to the page variable
  return page # returns the contents of the page variable


app.run(host='0.0.0.0', port=81)
