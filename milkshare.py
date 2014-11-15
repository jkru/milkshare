from flask import Flask, request, render_template, make_response
from flask import redirect, url_for, session, g, flash
import jinja2
import model


app = Flask(__name__)
app.secret_key = 'boobs'


@app.route("/")
def testthings():
    return render_template("home.html")


@app.route("/login")
def show_login():
    print "something"
    raw_input()
    return render_template("home.html")


@app.route("/main")
def show_main():
    return render_template("main.html")

@app.before_first_request
def setup_session():
    session.setdefault("logged_in", False)
    session.setdefault("email", None)

@app.before_request
def get_user():
    if session.get("email") is not None:
        g.logged_in = True
    else:
        g.logged_in = False

@app.route("/tryother")
def try_other():
    return render_template("crap.html")

@app.route("/login", methods=['POST'])
def actually_login():
    print "something else"
    temail = request.form.get("email")
    password = request.form.get("password")
    print password
    user = model.session.query(model.User).filter_by(email=temail).first()
    
    if user is None:
        print "none"
        flash("User does not exist")
        return redirect(url_for('actually_login'))
    elif user.password != password:
        flash("Incorrect password")
        print "incorrectpw"
        return redirect(url_for('actually_login'))
    else:
        session['email'] = user.email
        session['logged_in'] = True
        print "loggedin???"
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

@app.route("/milkexchange")
def milk_exchange_board():
    #this is where the database is going to live
    return render_template("donorlist.html")



if __name__ == "__main__":
    app.run(debug=True)

