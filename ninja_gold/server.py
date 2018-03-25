from flask import Flask, render_template, redirect, request, session, url_for
app = Flask(__name__)
app.secret_key = "secret"
import random, datetime

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
        session['running_total'] = 0
        session['desc'] = []
        session['activities'] = ""

    return render_template('index.html', rt = session['running_total'], desc = session['desc'])

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == "farm":
        x = random.randrange(10, 21)
        session['activities'] = "Earned {} golds from the farm! {}".format(x, datetime.datetime.now())

    elif request.form['building'] == "cave":
        x = random.randrange(5, 10)
        session['activities'] = "Earned {} golds from the cave! {}".format(x, datetime.datetime.now())
        
    elif request.form['building'] == "house":
        x = random.randrange(2, 5)
        session['activities'] = "Earned {} golds from the house! {}".format(x, datetime.datetime.now())

    elif request.form['building'] == "casino":
        x = random.randrange(-50, 51)
        if x < 0:
            session['activities'] = "Entered a casino and lost {} golds..Ouch! {}".format(x, datetime.datetime.now())
        elif x > 0:
            session['activities'] = "Earned {} golds from the casino! {}".format(x, datetime.datetime.now())


    session['running_total'] += x
    print "Running total is {}".format(session['running_total'])
    session['desc'].append(session['activities'])
    print session['activities']
    print session['desc']
    session['counter'] += 1
    return redirect ('/')
        
@app.route('/reset')
def reset():
    session.pop('counter')
    return redirect ('/')
    
app.run(debug=True)

