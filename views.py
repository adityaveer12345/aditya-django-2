from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request, _=None):
    jobs=Job.objects
    return render(request,'jobs/home.html',{ 'jobs':jobs})
