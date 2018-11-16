from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import Context, Template
from django.template.loader import get_template
from .models import Project

def index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, 'projects/index.html', context)
