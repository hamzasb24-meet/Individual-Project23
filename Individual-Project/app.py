from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {  "apiKey": "AIzaSyC7sGcQuisOfwb8Uv3Qkaaj3187CfMt5v8",
  "authDomain": "hamzaproject-f2e1f.firebaseapp.com",
  "projectId": "hamzaproject-f2e1f",
  "storageBucket": "hamzaproject-f2e1f.appspot.com",
  "messagingSenderId": "283981295731",
  "appId": "1:283981295731:web:9be289a5ae7d9a7ae2fa06",
 "databaseURL":"https://hamzaproject-f2e1f-default-rtdb.europe-west1.firebasedatabase.app/"}

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error =""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try:
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        user = {
        "email":email,
        "password":password
        }
        UID = login_session['user']['localId']
        db.child("Users").child(UID).set(user)
        # user=db.child("Users").child(UID).get().val()
        return redirect(url_for('home'))
    except:
        error = "Authentication failed"
        return  render_template("signup.html")
   
   return render_template("signup.html")




@app.route('/home', methods=['GET', 'POST'])
def home():
    UID = login_session['user']['localId']
    user=db.child("Users").child(UID).get().val()
    return render_template("index.html", user=user)

if __name__ == '__main__':
    app.run(debug=True)
