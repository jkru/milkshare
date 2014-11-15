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

