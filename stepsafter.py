import googlemaps
from flask import Flask, render_template, request, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/after-an-od')
def after_an_od():
    return render_template('after-an-od.html')

@app.route('/facilities')
def facilities():
    return render_template('facilities.html')

@app.route('/help')
def hello():
    return 'Text (424) 297-5085 for immediate instructions on dealing with an overdose.'
