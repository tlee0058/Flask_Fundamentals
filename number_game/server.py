from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
        # resets everything to play again
        session['number'] = random.randrange(0, 101)
        session['guess'] = False
        session['clue'] = ""
        
        print session['number']
        print session['guess']

    
    
    return render_template('index.html', guess=session['guess'], clue=session['clue'])



@app.route('/action', methods=['POST'])
def submit_form():
    
    print "Guess = {} Number = {}".format(request.form['guess'], session['number'])
    if int(request.form['guess']) > session['number']:
        print "Too high"
        session['guess'] = False
        session['clue'] = "Too High, Guess Again!"
    elif int(request.form['guess']) < session['number']:
        print "Too low"
        session['guess'] = False
        session['clue'] = "Too Low, Guess Again!"
    elif int(request.form['guess']) == session['number']:
        print "correct"
        session['guess'] = True
        session['clue'] = "Correct! The number was {}, it took you {} tries, Play again?".format(session['number'],session['counter'])
    session['counter'] +=1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def play_again():
    session.pop('counter')
    return redirect('/')

app.run(debug=True)
