from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route('/')
#def home():
#    return 'Hello, World!!!'

@app.route('/', methods=['GET', 'POST'])
def MainHandler():
    return render_template("index.htm", wordlength="", letters="", filters="")

@app.route('/about')
def about():
    return 'About'
