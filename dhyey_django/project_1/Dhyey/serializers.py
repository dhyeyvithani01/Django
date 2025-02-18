from rest_framework import serializers
from .models import *
import re

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
        # if data ["Email_id"] == '@gmail.com':
        #     raise serializers.ValidationError("Email Is Not Valid")
        
        if email[0].isdigit():
            raise serializers.ValidationError("Email Is Not Valid")
        
        elif not email.islower():
            raise serializers.ValidationError("Email Is Not Valid")
              
        elif not email.endswith('@gmail.com'):
            raise serializers.ValidationError("Email Is Not Valid")
        
        #mobile no validation
        mobile = data.get("Mobile_no")
        if  len(mobile)!=10 or not mobile.isdigit():
            raise serializers.ValidationError("Mobile number is not valid")
        
        #Password validation
        password =data.get("Password")
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        elif not any(char.isdigit() for char in password):
            raise serializers.ValidationError("Password must contain at least one digit")
        elif not any(char.isupper() for char in password):
            raise serializers.ValidationError("Password must contain at least one uppercase letter")
        elif not any(char.islower() for char in password):
            raise serializers.ValidationError("Password must contain at least one lowercase letter")
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>_]', password):
            raise serializers.ValidationError("Password must contain at least one special character")
        
        #Confirm password validation
        if data['Password'] != data["Confirm_password"]:
            raise serializers.ValidationError('Password Is Wrong')
        
        return data
        
# class Teacherserializers(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields ="__all__"