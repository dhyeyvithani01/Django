from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import json
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# @api_view(['Get'])
# def School(request):
#     obj=Student.objects.all()
#     serializer=Studentserializers(obj,many=True)
#     return Response({'status':200,'message':'right','payload':serializer.data})




# @api_view(['Get'])
# def Schooll(request):
#     obj=Teacher.objects.all()
#     serializer=Teacherserializers(obj,many=True)
#     return Response({'status':200,'message':'right','payload':serializer.data})



# @api_view(['POST'])
# def post(request):
#     data = request.data
#     serializer = Studentserializers(data = request.data)
#     if not serializer.is_valid():
#         return Response({'status' : 201,'massage' : 'wrong'})
#     serializer.save()
#     return Response({'STATUS' : 200,'MASSAGE' : 'RIGHT', 'PAYLOAD' : serializer.data})




# @api_view(['PUT'])
# def putt (requst,id):
#     try:
#         obj=Student.objects.get(id=id)
#         serializer=Studentserializers(obj,data=requst.data)
#         if not serializer.is_valid():
#             return Response({'status': 201, 'message':'WRONG'})
#         serializer.save()
#         return Response ({'status':200, 'massage':'RIGHT','payload': serializer.data})
#     except Exception as a :
#         return Response({'status':403,'massage':'ERROR'})

    
# @api_view(['PATCH'])
# def patchh (requst,id):
#     try:
#         obj=Student.objects.get(id=id)
#         serializer=Studentserializers(obj,data=requst.data,partial = True)
#         if not serializer.is_valid():
#             return Response({'status': 201, 'message':'WRONG'})
#         serializer.save()
#         return Response ({'status':200, 'massage':'RIGHT','payload': serializer.data})
#     except Exception as d :
#         return Response({'status':403,'massage':'ERROR'})
    
    
# @api_view(['DELETE'])
# def deletee(request,id):
#     try:
#         obj=Student.objects.get(id=id)
#         obj.delete()
#         return Response({'status': 200, 'message':"Right"})
#     except Exception as A :
#         return Response({'status':403,'message':'Wrong'})



def gett (request,var):
    obj = student.objects.get(id=var)
    serializer = studentserializers(obj)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type= 'application/json')
    #return JsonResponse(serializer.data)



def gettt (request):
    obj = student.objects.all()
    serializer = studentserializers(obj,many =True)
    json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type=' application/json')
    return JsonResponse(serializer.data,safe=False)


        
         
@api_view(['GET', 'POST'])
def my_get_view(request):
    if request.method == 'GET':
        obj = student.objects.all()
        serializer = studentserializers(obj,many =True)
        return JsonResponse(serializer.data,status=200,safe=False)
    
    elif request.method == 'POST':
        data =request.data 
        serializer = studentserializers(data =request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status = 400,safe=False)
        serializer.save()
        return Response(serializer.data,status=201,safe= False)