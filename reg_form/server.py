from flask import Flask, render_template, redirect, request, session, flash
import re, time
app = Flask(__name__)
app.secret_key = "secret"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0


    
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    session['email'] = request.form['email']

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email")
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1:
        flash("First name or last name cannot be blank")
    if request.form['password'] != request.form['confirm_pw']:
        flash("Passwords do not match")

    
    if len(request.form['password']) < 1:

        flash("Password cannot be blank")

    else:
        if len(request.form['password']) < 8:
            flash("Password must be at least 8 characters")
        else:
            if request.form['password'].isalpha():
                flash("Password must be at least one number")
            if request.form['password'].islower():
                    flash("Password must have at least one uppercase")

                

    flash("Thank you for submitting the form") 


    session['counter'] += 1
    return redirect ('/')


#     All fields are required and must not be blank
# First and Last Name cannot contain any numbers
# Password should be more than 8 characters
# Email should be a valid email
# Password and Password Confirmation should match
# Ninja Version:
# Add the validation that requires a password to have at least 1 uppercase letter and 1 numeric value.

# Hacker Version:
# Add a birth-date field that must be validated as a valid date and must be from the past.



app.run(debug=True)