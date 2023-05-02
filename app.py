from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/drevo')
def drevo():
    return render_template("drevo.html")

@app.route('/arhiv')
def arhiv():
    return render_template("arhiv.html")

@app.route('/rog')
def rog():
    return render_template("rog.html")

@app.route('/reg')
def reg():
    return render_template("reg.html")

@app.route('/n')
def n():
    return render_template("n.html")



@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + " - " +str(id)


if __name__ == "__main__":
    app.run()