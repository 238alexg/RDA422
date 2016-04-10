from mongoengine import connect
from models import RideRequest
from datetime import datetime
import operator
connect('saferide')


r = RideRequest(name="Rider", uoid=951000000, pickup_time=datetime.now(),
                     dropoff_time=datetime.now(), pickup_addr="Some place",
                     dropoff_addr="Other place")
#
# print r.uoid, r.name, r.pickup_addr, r.pickup_time, r.dropoff_addr, r.dropoff_time
#
#


def save_ride(ride):
    if type(ride) == RideRequest:
        ride.save()
        return ride
    elif type(ride) == type(dict):
        r = RideRequest(**ride)
        r.save()
        return r
    else:
        return None

def list_rides():
    for r in RideRequest.objects:
        print r

def get_ride_list(key=None):
    return sorted(RideRequest.objects, key=operator.itemgetter(key if key else "pickup_time"))
