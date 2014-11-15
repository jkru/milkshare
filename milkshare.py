from flask import Flask, request, render_template, redirect
from flask import session as user_session


app = Flask(__name__)

@app.route("/")
def note():
	return render_template("home.html")





if __name__=="__main__":
	app.run(debug = True)