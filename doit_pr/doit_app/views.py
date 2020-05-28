
from django.http import HttpResponse
import random
from .models import Task
from django.shortcuts import get_object_or_404, render


def index(request):

    return render(request, 'doit_app/home.html')# Create your views here.

def start(request):
    tot = Task.objects.count()
    n = random.randint(1,tot)
    task = Task.objects.get(pk=n).description
    task_age = Task.objects.get(pk=n).task_age
    context = {'tot':tot,'n':n,'task':task,'task_age':task_age}
    return render(request, 'doit_app/start.html', context)
