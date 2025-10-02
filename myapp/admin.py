from django.contrib import admin
from .models import CustomUser, Project, Task

admin.site.register([CustomUser, Project, Task])    
