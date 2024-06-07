from django.shortcuts import render
from django.http import HttpResponse  #for returing a http response 

# Create your views here.




def home(request):
    return HttpResponse("HOme")