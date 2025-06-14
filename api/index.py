from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!!!'

@app.route('/about')
def about():
    return 'About'
