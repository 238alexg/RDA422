#app.py

from flask import Flask, render_template, request as req, url_for
from flask.ext.mongoengine import MongoEngine
from werkzeug.contrib.fixers import ProxyFix
from datetime import datetime


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
    print(name, type(name))

    uoid = int(req.form.get('id').encode('utf-8'))
    print(uoid, type(uoid))

    phone = req.form.get('phone').encode('utf-8')
    print(phone, type(phone))

    pickup = req.form.get('pick_up').encode('utf-8')
    print(pickup, type(pickup))

    dropoff = req.form.get('drop_off').encode('utf-8')
    print(dropoff, type(dropoff))

    new_hour = int(req.form.get('hours').encode('utf-8'))
    print(new_hour, type(new_hour))

    new_minute = int(req.form.get('minute').encode('utf-8'))
    print(new_minute, type(new_minute))

    numRiders = int(req.form.get('riders').encode('utf-8'))
    print(numRiders, type(numRiders))

    specRequests = req.form.get('spec').encode('utf-8')
    print(specRequests, type(specRequests))
	# print("unexpected indent")

    # Set the pickup time to the one on the form
    pick_time = datetime.now()
    #print(pick_time)
    updated_time = pick_time.replace(hour=new_hour, minute=new_minute, second=0, microsecond=0)
    #print(updated_time)

    save_ride({"name":name,"uoid":uoid,"pickup_addr":pickup,"pickup_time":updated_time,"dropoff_addr":dropoff,"dropoff_time":datetime.now(),"group_size":numRiders,"special":specRequests})
    print("saved the ride info")
    return render_template('success.html')

if __name__ == "__main__":
    app.run(port=7771,host="0.0.0.0")
