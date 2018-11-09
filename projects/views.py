from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import Context, Template
from django.template.loader import get_template

def index(request):
    return HttpResponse('<h1>hello world!</h1>')
