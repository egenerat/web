from flask import Flask, make_response, request
app = Flask(__name__)

@app.route('/set-cookies')
def index():
    resp = make_response('Set two cookies')
    resp.set_cookie('username', 'John')
    resp.set_cookie('password', 'pa55w0rd', samesite='Strict')
    return resp

@app.route('/get-cookies')
def index2():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    return "Cookies received:<br/>Username: {}<br/>Password:{}".format(username, password)