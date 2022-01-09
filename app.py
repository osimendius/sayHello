from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
    flash("Please type your name here:")
    return render_template("index.html")

@app.route("/greet",methods=["POST","GET"])
def gree():
    flash("Hi "+str(request.form['name_input']) + ", great to see you.")
    return render_template("index.html")