from django.shortcuts import render
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from .models import *
from .serializers import*
import json
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

def gett (request,var):
    obj = student.objects.get(id=var)
    serializer = studentserializers(obj)
    json_data=JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type= 'application/json')
    return JsonResponse(serializer.data)



def gettt (request):
    obj = student.objects.all()
    serializer = studentserializers(obj,many =True)
    json_data=JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type=' application/json')
    return JsonResponse(serializer.data,safe=False)


        
         
# @api_view(['GET', 'POST'])
# def my_get_view(request):
#     if request.method == 'GET':
#         obj = student.objects.all()
#         serializer = studentserializers(obj,many =True)
#         return JsonResponse(serializer.data,status=200,safe=False)
    
#     elif request.method == 'POST':
#         data =request.data 
#         serializer = studentserializers(data =request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors,status = 400,safe=False)
#         serializer.save()
#         return Response(serializer.data,status=201,safe= False)
 