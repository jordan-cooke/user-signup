from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

        

@app.route("/", methods=['post'])
def index_submitted():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    verify_password = request.form['verify']
    username_stay = ''
    email_stay = ''
    password_error = ''
    username_error = ''
    verify_error = ''
    email_error = ''
    username_check = False
    password_check = False
    verify_check = False
    email_check = False

    #Username Check
    if len(username) > 20 or len(username) < 3:
        username_error = 'Username length out of range. Length must be between 3-20 characters.'
        username_stay = username
    else:
        username_check = True
        username_stay = username
    
    #Password Check
    if len(password) > 20 or len(password) < 3:
        password_error = 'Password length out of range. Length must be between 3-20 characters.'
    else:
        password_check = True

    #Verify Password
    if password != verify_password:
        verify_error = "Passwords don't match."
    else:
        verify_check = True

    #Email Check
    email_stay = email
    if email == '':
        email_check = True
    requirment_counter = 0
    if '@' in email:
        requirment_counter += 1
    if '.' in email:
        requirment_counter += 1
    if ' ' not in email:
        requirment_counter += 1
    if len(email) <= 20 and len(email) >= 3:
        requirment_counter += 1
    if requirment_counter == 4:
        email_check = True
    if email_check == False:
        email_error = "Invalid email. Must contain '@' and '.' and be over 3 characters long."

    print(username_check, password_check, verify_check, email_check)
    if username_check is True and password_check is True and verify_check is True and email_check is True:
        return redirect("/welcome?username={0}".format(username))
    return render_template('index.html', username_stay=username_stay, username_error=username_error, password_error=password_error, verify_error=verify_error, email_stay=email_stay, email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template('welcome.html', username=username)


app.run()
