''' Assignment: Counter
Build a flask application that counts the number of times the root route ('/') has been viewed. 
This assignment is to test your understanding of session.
* Ninja Level 1: Add a +2 button underneath the counter that reloads the page and increments counter by 2. Add another route to handle this functionality.
* Ninja Level 2: Add a reset button that resets the counter back to 1. Add another route to handle this functionality. '''

from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")

def index():
    if 'counter' not in session:
        session['counter'] = 0
        
    else:
        session['counter'] += 1
        
    
    return render_template("index.html", counter=session['counter'])



# Ninja Level 1
# Add a +2 button underneath the counter that reloads the page and increments counter by 2. Add another route to handle this functionality.
@app.route('/double', methods=["POST"])
def double():
    session['counter'] += 2
    return render_template("index.html", counter=session['counter'])


# Ninja Level 2
# Add a reset button that resets the counter back to 1. Add another route to handle this functionality.
@app.route('/clear')
def clear():
    session.clear()
    return redirect ("/")

app.run(debug=True)
