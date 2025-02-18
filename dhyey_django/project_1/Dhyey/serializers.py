from rest_framework import serializers
from .models import *

class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ="__all__"
        
# class Teacherserializers(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields ="__all__"