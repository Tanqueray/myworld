from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def index(request):
#    return HttpResponse("Hello world!")

def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())