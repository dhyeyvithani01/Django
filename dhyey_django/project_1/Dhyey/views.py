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




# @api_view(['Get'])
# def Schooll(request):
#     obj=Teacher.objects.all()
#     serializer=Teacherserializers(obj,many=True)
#     return Response({'status':200,'message':'right','payload':serializer.data})



# @api_view(['POST'])
# def demos(request):
#     data = request.data
#     serializer = Teacherserializers(data = request.data)
#     if not serializer.is_valid():
#         return Response({'status' : 201,'massage' : 'wrong'})
#     serializer.save()
#     return Response({'STATUS' : 200,'MASSAGE' : 'RIGHT', 'PAYLOAD' : serializer.data})




@api_view(['PUT'])
def putt (requst,id):
    try:
        obj=Student.objects.get(id=id)
        serializer=Studentserializers(obj,data=requst.data)
        if not serializer.is_valid():
            return Response({'status': 201, 'message':'WRONG'})
        serializer.save()
        return Response ({'status':200, 'massage':'RIGHT','payload': serializer.data})
    except Exception as a :
        return Response({'status':403,'massage':'ERROR'})