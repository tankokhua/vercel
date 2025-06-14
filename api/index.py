from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!!!'

@app.route('/result')
def result():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template("result.html", result = dict)

@app.route('/about')
def about():
    return 'About'

@app.route('/4p1w', methods=['GET', 'POST'])
def MainHandler():
    return render_template("index.htm", wordlength="", letters="", filters="")
