from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def company(request):
    return Response({'status':200,'message':'right'})



@api_view(['POST'])
def demos(request):
    data = request.data
    serializer = Studentserializers(data = request.data)
    if not serializer.is_valid():
        return Response({'status' : 201,'massage' : 'wrong'})
    serializer.save()
    return Response({'STATUS' : 200,'MASSAGE' : 'RIGHT', 'PAYLOAD' : serializer.data})