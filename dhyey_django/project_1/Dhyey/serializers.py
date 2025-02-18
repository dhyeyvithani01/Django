from rest_framework import serializers
from .models import *

class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ="__all__"
        
    def validate(self,data):
        
        # Name Validtion
        if not data["Name"].isalpha():
            raise serializers.ValidationError("Name must only contain alphabates")
        
        # Age validation
        if data["Age"]<18:
            raise serializers.ValidationError("The person must be at least 18 years old")
        
        #Email validation
        email=data.get("Email_id")
        if data ["Email_id"] == '@gmail.com':
            raise serializers.ValidationError("Email Is Not Valid")
        
        elif email[0].isdigit():
            raise serializers.ValidationError("Email Is Not Valid")
        
        elif not email.islower():
            raise serializers.ValidationError("Email Is Not Valid")
              
        elif not email.endswith('@gmail.com'):
            raise serializers.ValidationError("Email Is Not Valid")
        
        return data
        
# class Teacherserializers(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields ="__all__"