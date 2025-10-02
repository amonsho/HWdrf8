from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'
    USER = 'USER'

    CHOICES = [
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (USER, 'User')
    ]
    role = models.CharField(max_length=20, choices=CHOICES, default=USER)

    def __str__(self):
        return self.username
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='tasks')
    assigne = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, related_name='tasks')
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
