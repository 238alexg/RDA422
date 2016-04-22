#app.py

from flask import Flask, render_template, request as req, url_for
from flask.ext.mongoengine import MongoEngine
from datetime import datetime
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config["MONGODB_SETTINGS"] = {'DB': "saferide"}
app.config["SECRET_KEY"] = "thisisasecret"

from mongo.db import save_ride, get_ride_list, delete_ride

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
	return render_template('index.html')

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if req.form:
        #Need to delete ride
	ride_id = req.form.get("id")
        print("Deleting ride with id:", ride_id)
        if ride_id:
            delete_ride(ride_id)

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

    # hour = int(req.form.get('hours').encode('utf-8'))
    # print(hour, type(hour))

    # minute = int(req.form.get('minute').encode('utf-8'))
    # print(minutes, type(minutes))

    numRiders = int(req.form.get('riders').encode('utf-8'))
    print(numRiders, type(numRiders))

    specRequests = req.form.get('spec').encode('utf-8')
    print(specRequests, type(specRequests))
	# print("unexpected indent")

    # Set the pickup time to the one on the form
    pickup_time = datetime.now()
    #pickup_time.replace(hour=hour, minute=minute)

    save_ride({"name":name,"phone":phone,"uoid":uoid,"pickup_addr":pickup,"pickup_time":datetime.now(),"dropoff_addr":dropoff,"dropoff_time":datetime.now(),"group_size":numRiders,"special":specRequests})
    print("saved the ride info")
    return render_template('success.html')

if __name__ == "__main__":
	app.run()
