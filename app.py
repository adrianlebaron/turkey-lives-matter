from flask import Flask, render_template
from flash-heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/pageTwo')
def hompageTwo():
    return render_template("pageTwo.html")

@app.route('/pageThree')
def pageThree():
    return render_template("pageThree.html")





if __name__ == '__main__':
    app.debug - True
    app.run()