from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Friend(models.Model):
    name = models.CharField(max_length=100, default=True)
    message = models.TextField(max_length=200, default=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default_profile_picture.jpg')
    # Add other fields as needed

    def __str__(self):
        return self.name   


class Message(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True) 
    is_sent = models.BooleanField(default=True)   

    def __str__(self):
        return f'Message from {self.friend.name}'    