from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/help')
def hello():
    return 'Text (424) 297-5085 for immediate instructions on dealing with an overdose.'
