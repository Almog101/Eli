from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<userid>")
def user(userid):
    return render_template("user.html", userid=userid)


app.run(debug=True)
