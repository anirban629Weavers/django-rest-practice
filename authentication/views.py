from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework import exceptions as rest_exceptions, response, decorators as rest_decorators, permissions as rest_permissions
from rest_framework_simplejwt import tokens, views as jwt_views, serializers as jwt_serializers, exceptions as jwt_exceptions
from core import serializers,models


User=get_user_model()

@csrf_exempt
def normalRegister(request):
    '''
        registerView is used to register a user
    '''
    if request.method=="POST":  
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            returnStatement=f'Oops! {email}, already registered!'
            return HttpResponse(returnStatement)
        else:
            user=User.objects.create(name=name,
                                     email=email,
                                     password=password)
            returnStatement=f'Congratulations {user.name}!, You are now registered!'
            return HttpResponse(returnStatement)
    
    return HttpResponse("GET REQUEST NOT ALLOWED")


@rest_decorators.api_view(["POST"])
def registerView(request):  
    serializer = serializers.RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    if user is not None:
        return response.Response("Registered!")
    return rest_exceptions.AuthenticationFailed("Invalid credentials!")
