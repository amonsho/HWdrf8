from rest_framework.permissions import BasePermission
from .models import CustomUser

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == CustomUser.ADMIN
    

class IsManagerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == CustomUser.ADMIN:
            return True
        if request.user.role == CustomUser.MANAGER and obj.owner == request.user:
            return True
        return False
    

class ViewOrChangeTask(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == CustomUser.ADMIN:
            return True
        
        if request.user.role == CustomUser.MANAGER and obj.project.owner == request.user:
            return True
        
        if request.user.role == CustomUser.USER:
            if request.method in ('GET'):
                return True
            return obj.assigne == request.user
        return False