from flask import Flask, redirect, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup_form.html')

@app.route('/', methods=['POST'])
def submitted():

    username = request.form['username']
    password = request.form['password']
    v_password = request.form['v_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    v_password_error = ''
    email_error = ''

    if username == '':
        username_error = 'Please enter a Username.'
    if len(username) < 3 or len(username) > 20:
        username_error = 'Your username must be more than 3 characters and less than 20 characters.'
    if ' ' in username:
        username_error = 'Your username cannot contain any spaces.'

    if password == '':
        password_error = 'Please enter a Password.'
    if len(password) < 3 or len(password) > 20:
        password_error = 'Your username must be more than 3 characters and less than 20 characters.'
    if ' ' in password:
        password_error = 'Your password cannot contain any spaces.'

    if v_password == '':
        v_password_error = 'Please re-enter your Password.'

    if password != v_password:
        password_error = ''
        v_password_error = 'Please verify with a correct password.'

    # TODO:
    # add email conditions to validation

    if username_error == password_error and v_password_error == email_error:
        return redirect('/welcome')

    else:
        return render_template('signup_form.html', username=username, email=email,
            username_error=username_error, password_error=password_error, 
            v_password_error=v_password_error, email_error=email_error)

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

app.run()