from mongoengine import connect
from models import RideRequest
from datetime import datetime
import operator
connect('saferide')


r = RideRequest(name="Rider", uoid=951000000, pickup_time=datetime.now(),
                     dropoff_time=datetime.now(), pickup_addr="Some place",
                     dropoff_addr="Other place", group_size=3)

def save_ride(ride):
    if type(ride) == RideRequest:
        print("saving the ride object")
        ride.save()
        return ride
    elif type(ride) == dict:
        print("saving the ride dict", ride)
        r = RideRequest(**ride)
        r.save()
        print("save successful")
        return r
    else:
        print("Error saving ride", type(ride))
        return None

def list_rides():
    for r in RideRequest.objects:
        print r

def get_ride_list(sort=None):
    return sorted(RideRequest.objects, key=operator.itemgetter(sort if sort else "pickup_time"))

# save_ride(r)
# list_rides()
