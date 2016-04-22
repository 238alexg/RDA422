from mongoengine import *

class RideRequest(Document):
    uoid = IntField(min_value=950000000, max_value=959999999,required=True)
    name = StringField(max_length=100,required=True)
    phone = StringField(max_length=15,required=True)
    pickup_time = DateTimeField(required=True)
    pickup_addr = StringField(required=True)
    dropoff_addr = StringField(required=True)
    group_size = IntField(min_value=1, max_value=3, required=True)
    special = StringField(max_length="200")

    def __repr__(self):
        pickup_time_str = self.pickup_time.strftime("%I:%M").lstrip("0")
        dropoff_time_str = self.dropoff_time.strftime("%I:%M").lstrip("0")
        return "%d - %s, %d from %s @ %s to %s @ %s" % (self.uoid,self.name,self.group_size,self.pickup_addr,pickup_time_str,self.dropoff_addr,dropoff_time_str)
    def __str__(self):
        return self.__repr__()
