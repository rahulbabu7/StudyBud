
#handles the routes of the app 

from django.urls import path
from . import views   #importing the views





urlpatterns = [
    path('',views.home,name ="home")   #adding name to the route is a best practice as it have many advantages  names help us to access a particular views
]