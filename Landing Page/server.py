from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/dojos/new')
def new():
    return render_template("new.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    return render_template('index.html', name=request.form['name'])

app.run(debug=True)