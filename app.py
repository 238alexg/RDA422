#app.py

from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {'DB': "saferide"}
app.config["SECRET_KEY"] = "thisisasecret"

from mongo.db import save_ride, get_ride_list

@app.route("/")
def main():
	save_ride({
			"name":"Rider",
			"uoid":951000000,
			"pickup_addr":"Some place",
			"pickup_time":datetime.now(),
			"dropoff_addr":"Other place",
			"dropoff_time":datetime.now(),
			"group_size":3
		})
	rides = get_ride_list()
	print("There are %d rides." % len(rides))
	for r in rides:
		print r
	return render_template('index.html')

@app.route("/list_rides")
def list_rides():
	rides = get_ride_list()
	return render_template('list_rides.html', rides=rides)

if __name__ == "__main__":
	app.run()
