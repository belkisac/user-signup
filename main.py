from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def validate_info():
    username = request.form['username']

    if len(username) < 3 or len(username) > 20:
        error = "That's not a valid username"
        return render_template('index.html', username_error=error)

    #password = request.form['password']
    #verify_password = request.form['verify-password']

    #if verify_password != password:
    #    error = "Passwords do not match"
    #    return redirect('/?error=' + error)

@app.route('/welcome')
def success():
    return render_template('welcome.html', username=username)

app.run()

