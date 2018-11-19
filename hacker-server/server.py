
from flask import Flask, render_template, request, session, redirect, url_for
import history

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/stealhistory", methods=['POST'])
def parent_login():
    if request.method == 'POST':
        email = request.form['email']
        url = request.form['url']
        time = request.form['last_visited']
        history.addToHistory(email, url, time)
        return "\n\n\nWe added to history: " + email

@app.route('/addSecure', methods=['POST'])
def add_secure():
    if request.method == 'POST':
        url = request.form['url']
        history.addToSecure(url)
        urls = history.getFromSecure()
        urls = map(lambda x: str(x[0]), urls)
        return render_template("index.html", urls=urls)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True # So template reloads when data is changed
    app.run(host='localhost', port=5000, debug=True)