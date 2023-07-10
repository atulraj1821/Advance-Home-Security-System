from django.http import JsonResponse
from .models import Known
from .models import Criminal
from .serializers import KnownSerializer
from .serializers import CriminalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
import base64
import os
from .models import Unknown
import pathlib
from pathlib import Path

# Creating Apis for get, post ,put and delete requests
@api_view(['GET', 'POST'])

#getting known list
#function
def known_list(request, format=None):

    # get all the people
    # serialize them
    # returnjson
    if request.method == 'GET':
        known = Known.objects.all()
        serializer = KnownSerializer(known, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = KnownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])

#getting known details 
def known_detail(request, id, format=None):

    try:
        known = Known.objects.get(pk=id)
    except Known.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = KnownSerializer(known)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = KnownSerializer(known, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = KnownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        known.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])

#getting criminal list
#function
def criminal_list(request, format=None):

    # get all the people
    # serialize them
    # returnjson
    if request.method == 'GET':
        criminal = Criminal.objects.all()
        serializer = CriminalSerializer(criminal, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CriminalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])

#getting criminal details 

def criminal_detail(request, id, format=None):

    try:
        criminal = Criminal.objects.get(pk=id)
    except Criminal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CriminalSerializer(criminal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CriminalSerializer(criminal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = CriminalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        criminal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# function to render the main page of django
def mainpage(request):
    return render(request ,'main.html')

# function to render the unknown images page

def unknownlist(request):
    if request.user.is_anonymous:
        return redirect('/error')
    
    # getting path of unknown images    
    path = pathlib.Path(__file__).parent.parent/ r'media\unknownimg'
    img_list = os.listdir(path)

    # rendering html page
    return render(request, 'index.html', {'images':img_list})

# function to render the known images page

def knownlist(request):
    if request.user.is_anonymous:
        return redirect('/error')

    # getting path of known images
    path = pathlib.Path(__file__).parent.parent/ r'media\knownimg'
    img_list = os.listdir(path)

    # rendering html page
    return render(request, 'known.html', {'images':img_list})

# function to render the criminal images page

def criminallist(request):
    if request.user.is_anonymous:
        return redirect('/error')
        
    # getting path of criminal images    
    path = pathlib.Path(__file__).parent.parent/ r'media\criminalimg'
    img_list = os.listdir(path)

    # rendering html page
    return render(request, 'criminal.html', {'images':img_list})
 
