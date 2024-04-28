from flask import Flask, render_template, url_for
app = Flask(__name__)


To_do = ["chame shaurma", "codi dawere", "davalebebi gaakete", "compiuteri dalewe", "daidzine"]


@app.route('/')
def home():
    return render_template('index.html', To_do=To_do)


@app.route('/add_task')
def add_task():
    return render_template("add_task.html")


if __name__ == "__main__":
    app.run(debug=True)
