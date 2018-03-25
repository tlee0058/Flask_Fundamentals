from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "secret"
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html')


@app.route('/action', methods=['POST'])
def action():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['dojo'] = request.form['dojo']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print request.form
    form_complete = True

    if len(session['name']) < 1:
        flash("Name or Comments cannot be blank")
        form_complete = False
    if len(session['comment']) > 121:
        flash("Comments must be less than 120 characters")
        form_complete = False

    
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email is invalid")
        form_complete = False



    if form_complete:
        
        session['counter'] += 1
        return redirect("/success")
    else:
        return redirect ('/')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route("/reset")
def reset():
    session.clear()
    return redirect ('/')


app.run(debug=True)