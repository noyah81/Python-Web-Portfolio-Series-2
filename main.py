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
@app.route('/videos')
def video():
    return render_template("videos.html")


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

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='5000', host='127.0.0.1')
    #KK