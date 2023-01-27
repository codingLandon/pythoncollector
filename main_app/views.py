from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import Python

def home(request):
  return render(request, 'about.html')

def about(request):
  return render(request, 'about.html')

def pythons_index(request):
    pythons = Python.objects.all()
    return render(request, 'pythons/index.html', { 'pythons': pythons })

def pythons_detail(request, python_id):
    python = Python.objects.get(id=python_id)
    return render(request, 'pythons/detail.html', { 'python': python })

class PythonCreate(CreateView):
  model = Python
  fields = '__all__'
