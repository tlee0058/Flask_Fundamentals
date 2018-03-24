from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def create():
    return render_template('result.html', name=request.form['name'], location=request.form['location'], language=request.form['language'], desc=request.form['desc'])

app.run(debug=True)
