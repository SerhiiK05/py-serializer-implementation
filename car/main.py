import io

from django.db.models.functions import JSONObject
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car):
    serializer = CarSerializer(car)
    if serializer.is_valid():
        json = JSONRenderer().render(serializer.data)
        return json
    raise ValidationError("Value should be similar to Car model")


def deserialize_car_object(json: JSONObject) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        car = serializer.save()
        return car
    raise ValidationError("Value should be similar to Car model")
