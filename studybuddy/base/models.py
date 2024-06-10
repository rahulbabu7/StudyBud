from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
    

class Message(models.Model):

    room = models.ForeignKey(Room,on_delete=models.CASCADE)  #when room gets deleted all the children gets deleted
    body =models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.body[0:50])