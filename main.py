from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
# Validators doc pages: https://wtforms.readthedocs.io/en/2.3.x/validators/
from wtforms.validators import DataRequired, Email, Length

"""
The code snippet 'class LoginForm(FlaskForm)': 
-  indicates the creation of a web form for a Flask application, specifically a login form. This
form utilizes the Flask-WTF extension, which integrates WTForms with Flask to simplify
  form handling and validation.
Explanation:
FlaskForm Inheritance:
  - LoginForm inherits from FlaskForm, a base class provided by Flask-WTF. This inheritance 
grants LoginForm access to the functionalities and methods necessary for handling form 
submissions, validation, and rendering within a Flask environment.
  - Form Fields:
    Within the LoginForm class, you would define the individual fields of the form as class 
variables. For a login form, these commonly include:
-- username: Typically a StringField for text input.
-- password: A PasswordField for secure password input.
-- remember_me: Optionally, a BooleanField for a "remember me" checkbox.
-- submit: A SubmitField to create a submit button.
  - Validators:
    Each field can be assigned validators from wtforms.validators to enforce rules on the input 
data (e.g., DataRequired() to ensure a field is not empty, Length() to specify minimum/maximum length).

- This LoginForm class would then be used in a Flask route to create an instance of the form, handle 
its submission, and process the collected data.

"""
class LoginForm(FlaskForm):
    """
    In essence, this line of code defines an "Email" input field that is
    mandatory and requires the user to enter an email address >= 6 and
    stops at 30 characters in length. This is a basic form of input validation to
    ensure data quality and prevent common errors or malicious inputs.
    The label is displayed in the form.
    Installed 'email-validator' package to validate email address entries, signified below
    as part of the 'email' definition, Email()
    """
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6,max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30)])
    """
    Provides for a button with the name 'login' that will 'submit' data entered in
    a form.
    -This line defines a specific field within a form class that, when rendered in HTML, will appear 
        as a button that a user can click to submit the form data to the server. 
    - For example, in a login form, this button would trigger the submission of the username and password 
        entered by the user.
    """
    submit = SubmitField('Login')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'l6h3d4drae'

@app.route("/")
def home():
    return render_template('index.html')

#@app.route("/login", methods=['GET', 'POST'])
#def login():
#    login_form = LoginForm()
#    return render_template('login.html', form=login_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() # Creates an object 'form' of 'Class' LoginForm
    # If the submission is a 'POST', any validations required take place
    # with the next line of code.  Returns 'True'' if data sent meets all
    # validations
    if form.validate_on_submit():
        email = request.form['email']
        # The line below performs the same as the line above!
        #email = form.email.data
        password = form.password.data
        #flash(f'Email: {email}, Password: {password} - Form submitted successfully!')
        # In a real application, you would typically verify credentials here.
        # When here, any validations are satisfied!
        if form.email.data == "rick0142@gmail.com" and form.password.data == "L6h3d4drae":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    # We arrive  here if there is any type of validation error!
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
