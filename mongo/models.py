from mongoengine import *

class RideRequest(Document):
    uoid = IntField(min_value=951000000, max_value=951999999,required=True)
    name = StringField(max_length=100,required=True)
    pickup_time = DateTimeField(required=True)
    dropoff_time = DateTimeField(required=True)
    pickup_addr = StringField(required=True)
    dropoff_addr = StringField(required=True)


    def __repr__(self):
        pickup_time_str = self.pickup_time.strftime("%I:%M").lstrip("0")
        dropoff_time_str = self.dropoff_time.strftime("%I:%M").lstrip("0")
        return "%d - %s, from %s @ %s to %s @ %s" % (self.uoid,self.name,self.pickup_addr,pickup_time_str,self.dropoff_addr,dropoff_time_str)
    def __str__(self):
        return self.__repr__()
