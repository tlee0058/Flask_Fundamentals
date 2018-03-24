from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
    return ("No ninjas here")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")



@app.route('/ninja/<ninja_color>')
def ninja_color(ninja_color):
    return render_template("ninja.html", ninja_color=ninja_color)

app.run(debug=True)