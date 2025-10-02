from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task,Project

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'role')

class TaskSerializer(serializers.ModelSerializer):
    assigne = UserSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title','project','assigne','is_done']


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'owner', 'tasks']
        read_only_fields = ['owner']


