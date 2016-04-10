#app.py

from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {'DB': "saferide"}
app.config["SECRET_KEY"] = "thisisasecret"

from mongo.db import save_ride, list_rides

@app.route("/")
def main():
	save_ride({"name":"Rider", "uoid":951000000, "pickup_time":datetime.now(),"dropoff_time":datetime.now(), "pickup_addr":"Some place","dropoff_addr":"Other place"})
	list_rides()
	return render_template('index.html')

if __name__ == "__main__":
	app.run()
