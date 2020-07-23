from django.db import models
from home.models import User
from django.contrib.sessions.models import Session

class messageManager(models.Manager):

    def postMessage(self, data, user):#gets the user passed to it
        return self.create( 
            message = data['message'],
            user = user)
       #this is wrong 

    def validation(self, data):
        error = {}
        if len(data['message']) < 15:
            error['message'] = "Gotta be at least 15 characters"
        return error

class commentManager(models.Manager):
    def validation(self, data):
        error = {}
        if len(data['comment']) < 15:
            error['comment'] = "Gotta be at least 15 characters"
        return error
    #TODO finish out the create method

class message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = messageManager()

class comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(message, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = commentManager()

