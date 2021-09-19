from django.db import models
#existing tables in database

class User(models.Model):
    usr = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

class User_Chat(models.Model): #one user to many chats
    usr = models.ForeignKey('User', on_delete=models.PROTECT) #the user should exist
    chat = models.BigIntegerField() #chat/channel id