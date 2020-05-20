from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
# from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Time_Period,User_Name
from .serializers import Time_PeriodSerializer,User_NameSerializer
# Create your views here.
@api_view(['GET'])
def user_data(request):
    user = User_Name.objects.all()
    serializer = User_NameSerializer(user,many=True)
    return Response(serializer.data)
