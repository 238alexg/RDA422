#app.py

from flask import Flask, render_template, request as req, url_for
from flask.ext.mongoengine import MongoEngine
from datetime import datetime
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config["MONGODB_SETTINGS"] = {'DB': "saferide"}
app.config["SECRET_KEY"] = "thisisasecret"

from mongo.db import save_ride, get_ride_list

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
	return render_template('index.html')

@app.route("/admin")
def admin():
    rides = get_ride_list()
    return render_template('admin.html', rides=rides)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/request")
def ask():
    return render_template('request.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/suc")
def suc():
    return render_template('success.html')

@app.route('/buttonPress', methods=['POST'])
def buttonPress():
    print("BUTTON HAS BEEN PRESSED")
    name = req.form.get('usr').encode('utf-8')
    uoid = int(req.form.get('id').encode('utf-8'))
    phone = req.form.get('phone').encode('utf-8')
    pickup = req.form.get('pick_up').encode('utf-8')
    dropoff = req.form.get('drop_off').encode('utf-8')
    hour = req.form.get('hour')
    minutes = req.form.get('min')
    numRiders = int(req.form.get('riders').encode('utf-8'))
    specRequests = req.form.get('spec').encode('utf-8')
    print(name, type(name))
    print(uoid, type(uoid))
    print(phone, type(phone))
    print(pickup, type(pickup))
    print(dropoff, type(dropoff))
    # print(hour, type(hour))
    # print(minutes, type(minutes))
    print(numRiders, type(numRiders))
    print(specRequests, type(specRequests))
	# print("unexpected indent")

    # Set the pickup time to the one on the form
    pickup_time = datetime.now()
    pickup_time.replace(hour=hour, minute=minutes)

    save_ride({"name":name,"uoid":uoid,"pickup_addr":pickup,"pickup_time":pickup_time,"dropoff_addr":dropoff,"group_size":numRiders,"special":specRequests})
    print("saved the ride info")
    return render_template('success.html')

if __name__ == "__main__":
	app.run()
