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
    print "showing log in"
    return render_template("home.html")


@app.route("/main")
def show_main():
    return render_template("main.html")


@app.route("/tryother")
def try_other():
    return render_template("crap.html")

@app.route("/login", methods=['POST'])
def actually_login():
    print "something else"
    email = request.form.get("email")
    password = request.form.get("password")
    print password
    #user = model.session.query(model.User).filter_by(email=temail).first()
    
    user = model.get_user_by_email(email, password)

    if user is None:
        print "none"
        flash("User does not exist")
        return redirect(url_for('actually_login'))
    #elif user.password != password:
    elif user == "incorrect password":
        flash("Incorrect password")
        print "incorrectpw"
        return redirect(url_for('actually_login'))
    else:
        session['email'] = user.email
        session['id'] = user.id
        session['logged_in'] = True
        print "loggedin???"
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    return render_template("main.html")


@app.route("/logout")
def log_out():
    session.clear()
    #session['logged_in'] = False
    return render_template("home.html")


@app.route("/createacct")
def create_acct():
    return render_template("createacct.html")


@app.route("/myprofile")
def myprofile():
    user_info = get_user_by_id(session['id'])
    return render_template("userprofile.html", user_info=user_info)

@app.route("/editprofile")
def editprofile():
    return render_template("edituserprofile.html")

@app.route("/milkexchange")
def milk_exchange_board():

    all_posts = model.get_posts()
    return render_template("stupid.html", all_posts=all_posts)
    #return render_template("donorlist.html", all_posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

