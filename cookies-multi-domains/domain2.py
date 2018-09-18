from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Second domain <a href="http://127.0.0.1:5000/get-cookies">Link to first domain</a>'
