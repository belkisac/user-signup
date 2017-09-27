from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def validate_info():
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['verify-password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''


    if len(username) < 3 or len(username) > 20 or username == '':
        username_error = "That's not a valid username"
        username = ''
    else:
        username = username

    if len(password) < 3 or len(password) > 20 or password == '' or ' ' in password:
        password_error = "That's not a valid password"

        if password2 != password or password2 == '':
            verify_error = "Passwords don't match"
    
    if email != '':
        if len(email) < 3 or len(email) > 20:
            email_error = "Please enter a valid email address"
            email = ''
        if '@' not in email or '.' not in email:
            email_error = "Please enter a valid email address"
            email = ''
        else:
            email = email
    
    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('index.html',username_error=username_error,
            password_error=password_error,verify_error=verify_error,email_error=email_error,
            username=username,email=email)




@app.route('/welcome')
def success():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()

