from flask import Flask, render_template
import os
import jinja2

#create a Flask instance
app = Flask(__name__)


#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")


#connect to videos page
@app.route('/video')
def video():
    return render_template("video.html")


#connects to calculator page
@app.route('/calculator')
def calulator():
    return render_template("calculator.html")


#connects to journals page
@app.route('/journals')
def journals():
    return render_template("journals.html")

@app.route('/quizzes')
def quizzes():
   return render_template("quizzes.html")

@app.route('/flask')
def flask():
  return render_template("flask.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='5000', host='0.0.0.0')
    #KK
    #Karam