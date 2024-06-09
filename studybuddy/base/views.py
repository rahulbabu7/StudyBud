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
    context = {'rooms':rooms}
    return render(request,'base/home.html',context) #This line attempts to render an HTML template
#The render function is a shortcut provided by Django to 
# combine a template with a context dictionary and 
# return an HttpResponse object with that rendered text.

def room(request,id):
    # return HttpResponse("Room")
    room = None
    for i in rooms:
        if i['id'] == int(id):
            room = i
    context = {'room':room}
    return render(request,'base/room.html',context)