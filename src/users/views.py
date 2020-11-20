from django.shortcuts import render

# Create your views here.

# This part of code below is copied from Lab 4 materials in Moodle.

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import requests

from .serializers import CreateUserSerializer


CLIENT_ID = 'OXyeRyKdRrI8qaFb9Pn5AyHGr0jJICz3mfbduulI'
CLIENT_SECRET = '9vM4RGaD2hUcVnzie5Pn36uvsFAYMqlSL2CGywdoWaSi21CSFjgoABE09PwEVwm48NcWgOwnzpeIYlaRb5LRuvAY84KcIEIWUKnrQPEDSShb0LLLwhnLC1TxboA9VFsp'


IP_token = 'http://193.61.36.109:8000/o/token/'  # for upload to BBK vm
IP_revoke_token ='http://193.61.36.109:8000/o/revoke_token/'  # for upload to BBK vm
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    # Put the data from the request into the serializer
    serializer = CreateUserSerializer(data=request.data)
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save()
        # Then we get a token for the created user.
        # This could be done differentley
        r = requests.post(IP_token,
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(r.json())
    return Response(serializer.errors)



@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    r = requests.post(
    IP_token,
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())



@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
    IP_token,
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        IP_revoke_token,
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise)
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)
