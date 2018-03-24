from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=["POST"])
def add():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['desc'] = request.form['desc']
    return redirect ('/success')

@app.route('/success')
def success():
    return render_template("result.html")

app.run(debug=True)
