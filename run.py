from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/myfavs')
def myfavs():
    return render_template('myfavs.html')