import json

from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.shortcuts import  render, redirect
from .models import WikiInformation, User

@login_required
def home(request):
    topics = WikiInformation.objects.all() #queryset containing all books we just created
    return render(request, "home.html", {'topics':topics})

def signup(request):
    return render(request, "signup.html")

@csrf_exempt
def signup_validate(request):
    body = json.loads(request.body)
    print("body = ",body)
    email = body.get("email", "")
    first_name = body.get("first_name", "")
    last_name = body.get("last_name", "")
    password = body.get("password", "")

    if not email:
        result = {"success": False, "message": "email not found"}
        return JsonResponse(result)

    if not first_name:
        result = {"success": False, "message": "first name not found"}
        return JsonResponse(result)
    try:
        User.objects.create(email=email, 
            first_name=first_name,
            last_name=last_name,
            password=password
        )
    except IntegrityError:
        result = {"success": False, "message": "user already exists"}
        return JsonResponse(result)

    result = {"success": True, "message": "User Created Successfully"}
    return JsonResponse(result)

def c_login(request):
    return render(request, "login.html")

@csrf_exempt
def login_validate(request):
    body = json.loads(request.body)
    print("body = ",body)

    email = body.get("email", "")
    password = body.get("password", "")

    try:
        user = User.objects.get(email=email)
    except ObjectDoesNotExist:
        result = {"success": False, "message": "please signup"}
        return JsonResponse(result)
    print(password)
    print(user.password)
    login(request, user)
    if user.password == password:
        result = {"success": True, "message": "login succeeded"}
        return JsonResponse(result)

@login_required
def c_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")

# Create your views here.
@csrf_exempt
def wikiinfo(request):
    body = json.loads(request.body)
    print("body = ",body)
    topic = body.get("topic", "")
    article = body.get("article", "")
    if not topic:
        result = {"success": False, "message": "topic not found"}
        return JsonResponse(result)

    if not article:
        result = {"success": False, "message": "article content not found"}
        return JsonResponse(result)
    try:
        WikiInformation.objects.create(topic=topic, article=article)
    except IntegrityError:
        result = {"success": False, "message": "Got error while creating new content"}
        return JsonResponse(result)

    result = {"success": True, "message": "Wiki knowledge saved successfully"}
    return JsonResponse(result)





