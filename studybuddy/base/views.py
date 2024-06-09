from django.shortcuts import render
from django.http import HttpResponse  #for returing a http response 

# Create your views here.

rooms = [
    {
        'id' : 1,
        'name' : 'lets learn python'
    },
       {
        'id' : 2,
        'name' : 'lets learn Django'
    },
   {
        'id' : 3,
        'name' : 'lets learn Vue'
    },


]




def home(request):
    # return HttpResponse("HOme")
    return render(request,'home.html') #This line attempts to render an HTML template
#The render function is a shortcut provided by Django to 
# combine a template with a context dictionary and 
# return an HttpResponse object with that rendered text.

def room(request):
    # return HttpResponse("Room")
    context = {'rooms':rooms}
    return render(request,'room.html',context)