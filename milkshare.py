from flask import Flask, request, render_template, make_response
from flask import redirect, url_for, session, g, flash
import jinja2
import model
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'boobs'


@app.route("/")
def testthings():
    return render_template("home.html")


@app.route("/login")
def show_login():
    return render_template("home.html")


@app.route("/main")
def show_main():
    return render_template("main.html")


@app.route("/tryother")
def try_other():
    return render_template("crap.html")

@app.route("/login", methods=['POST'])
def actually_login():
    email = request.form.get("email")
    password = request.form.get("password")

    #user = model.session.query(model.User).filter_by(email=temail).first()
    
    user = model.get_user_by_email(email, password)

    if user is None:
        flash("User does not exist")
        return redirect(url_for('actually_login'))
    elif user == "incorrect password":
        flash("Incorrect password")
        return redirect(url_for('actually_login'))
    else:
        session['email'] = user.email
        session['id'] = user.id
        session['logged_in'] = True
    return redirect(url_for("main_page"))


@app.route("/main")
def main_page():

    return render_template("main.html")

@app.route("/dashboard")
def dashboard():
    sent_messages = model.get_sent_messages(session['id'])
    received_messages = model.get_received_messages(session['id'])
    return render_template("dashboard.html",sent=sent_messages,received=received_messages)

@app.route("/logout")
def log_out():
    session.clear()
    return render_template("home.html")

@app.route("/createacct")
def display_create_acct():
    return render_template("createacct.html")


@app.route("/createacct", methods=['POST'])
def create_acct():
    first = request.form.get("first_name")
    last = request.form.get("last_name")
    email_in = request.form.get("email")
    password_in = request.form.get("password")
    zipcode_in = request.form.get("zipcode")
    baby_year = request.form.get("year")
    baby_month = request.form.get("month")
     

    u = model.User()
    u.first_name = first
    u.last_name = last
    u.email = email_in
    u.password = password_in
    u.zip_code = zipcode_in
    u.baby_dob = datetime.strptime(str(baby_year+"-"+baby_month+"-01").split()[0], "%Y-%m-%d")

    model.session.add(u)
    model.session.commit()
    return redirect(url_for("show_login"))

@app.route("/myprofile")
def myprofile():
    user_info = model.get_user_by_id(session['id'])
    return render_template("userprofile.html", user=user_info)

@app.route("/editprofile", methods=['GET'])
def load_editprofile():
    user = model.get_user_by_id(session['id'])
    return render_template("edituserprofile.html", user=user)

@app.route("/editprofile", methods=['POST'])
def editprofile():
    first = request.form.get("first_name")
    last = request.form.get("last_name")
    email_in = request.form.get("email")
    password_in = request.form.get("password")
    age = request.form.get("age")
    cell = request.form.get("cell_phone")
    zipcode = request.form.get("zip_code")
    dairy = request.form.get("dairy")
    wheat = request.form.get("wheat")
    soy = request.form.get("soy")
    caffeine = request.form.get("caffeine")
    alcohol = request.form.get("alcohol")
    health = request.form.get("health")
    drug = request.form.get("drug")
    about = request.form.get("about")
    notes = request.form.get("notes")

    u = model.get_user_by_id(session['id'])
    u.first_name = first
    u.last_name = last
    u.email = email_in
    u.password = password_in
    u.cell_phone = cell
    u.baby_dob = datetime.strptime(age, "%Y-%m-%d")
    u.zip_code = zipcode
    u.no_dairy = (dairy == "on")
    u.no_wheat = (wheat == "on")
    u.no_soy = (soy == "on")
    u.no_caffeine = (caffeine == "on")
    u.no_alcohol = (alcohol == "on")
    u.drug_info = drug
    u.has_health_info = (health == "on")
    u.about_me = about
    u.notes = notes
    model.session.commit()
    flash("Profile changes saved.")
    return redirect("/dashboard")

@app.route("/milkexchange")
def milk_exchange_board():
    all_posts = model.get_posts()
    return render_template("donorlist.html", all_posts=all_posts)

@app.route("/users/<int:user_id>")
def donor_profile(user_id):
    user = model.get_user_by_id(user_id)
    return render_template("donorprofile.html",user=user)

@app.route("/users/<int:user_id>/messages/")
def private_message(user_id):
    user = model.get_user_by_id(user_id)
    session['lookingat_id'] = user.id
    return render_template("message.html",user=user)

@app.route("/sendmessage", methods=['POST'])
def send_message():
    inmessage = request.form.get("inputmessage")
    senderid = session['id']
    recipientid = session['lookingat_id']
    insubject = request.form.get("subject")

    m = model.Message()
    m.sender_id = senderid
    m.recipient_id = recipientid
    m.date = datetime.strptime(str(datetime.now()).split()[0], "%Y-%m-%d")
    m.subject = insubject
    m.message = inmessage
    model.session.add(m)
    model.session.commit()

    return redirect(url_for("milk_exchange_board"))

@app.route("/newpost")
def display_new_post():
    return render_template("newpost.html")


@app.route("/newpost", methods=['POST'])
def new_post():

    req_or_off = request.form.get("req_or_off")
    amt_milk = request.form.get("amt_milk")
    recurring = request.form.get("recurring")
    blurb = request.form.get("blurb")


    p = model.Post()
    p.user_id = session['id']
    p.req_or_off = req_or_off
    p.date = datetime.strptime(str(datetime.now()).split()[0], "%Y-%m-%d")
    p.amt_milk = amt_milk
    p.recurring = recurring
    p.blurb = blurb

    model.session.add(p)
    model.session.commit()
    #return render_template("newpost.html")
    return redirect(url_for("milk_exchange_board"))

if __name__ == "__main__":
    app.run(debug=True)

