from flask import render_template, url_for

from ArtifactFiles import app

@app.route("/")
@app.route('/home')
def home():
    return render_template("home.html")


@app.route("/software")
def software():
    return render_template("software.html")


@app.route("/what_they_do")
def what_they_do():
    return render_template("what_they_do.html")


@app.route("/languages")
def languages():
    return render_template("languages.html")