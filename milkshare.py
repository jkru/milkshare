from flask import Flask, request, render_template, make_response
from flask import redirect, url_for, session, g, flash
import jinja2
import model


app = Flask(__name__)
secret_key = 'boobs'


@app.route("/")
def testthings():
    return render_template("home.html")


@app.route("/login")
def show_login():
    return render_template("home.html")


@app.route("/main")
def show_main():
    return render_template("main.html")


@app.route("/login", methods=['POST'])
def actually_login():
    email = request.form.get("email")
    password = request.form.get("password")
    user = model.get_user_by_email(email)
    if user == None:
        flash("User does not exist")
        return redirect(url_for('actually_login'))
    #elif (password != customer)
    else:
        session['email'] = user.email
    return render_template("home.html")


@app.route("/logout")
def log_out():
    return 


@app.route("/createacct")
def create_acct():
    return render_template("createacct.html")


@app.route("/userprofile")
def account():
    return render_template("userprofile.html")






if __name__ == "__main__":
    app.run(debug=True)

