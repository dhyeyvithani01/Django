from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['Get'])
def School(request):
    obj=Student.objects.all()
    serializer=Studentserializers(obj,many=True)
    return Response({'status':200,'message':'right','payload':serializer.data})



@api_view(['POST'])
def demos(request):
    data = request.data
    serializer = Teacherserializers(data = request.data)
    if not serializer.is_valid():
        return Response({'status' : 201,'massage' : 'wrong'})
    serializer.save()
    return Response({'STATUS' : 200,'MASSAGE' : 'RIGHT', 'PAYLOAD' : serializer.data})