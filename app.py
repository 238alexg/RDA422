#app.py

from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {'DB': "saferide"}
app.config["SECRET_KEY"] = "thisisasecret"

from mongo.db import save_ride, list_rides, get_ride_list
from mongo.models import RideRequest
import operator
@app.route("/")
def main():
	rides = get_ride_list()

	for r in rides:
		print r
	return render_template('index.html')

if __name__ == "__main__":
	app.run()
