from rest_framework import serializers
from .models import *

class Studentserializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(default=20)
    address = serializers.CharField(max_length =100)
    email = serializers.EmailField(default='')