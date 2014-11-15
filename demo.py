<<<<<<< HEAD
from flask import Flask, request, render_template, redirect
from flask import session as user_session


app = Flask(__name__)

@app.route("/")
def note():
	return render_template("home.html")





if __name__=="__main__":
	app.run(debug = True)
=======
from flask import Flask, request, render_template, make_response
from flask import redirect, url_for
import jinja2
import model


app = Flask(__name__)
secret_key = 'boobs'

@app.route("/")
def testthings():
    return render_template("test_oauth.html")

@app.route("/account")
def account():
    
    return render_template("account_page.html")
if __name__ == "__main__":
    app.run(debug=True)

>>>>>>> 8c2611ebbef2b6e3e310c8c431b7750add92c6d8
