from django.shortcuts import render

# Create your views here.
from ninja import ModelSchema

from location.models import Location



class LocationSchema(ModelSchema):

    class Config:
        model = Location
        model_fields = "__all__"
