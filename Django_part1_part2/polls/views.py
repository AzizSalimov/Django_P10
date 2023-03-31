from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, World. You're at the polls <span style='color:red'>index</span></h1>")

