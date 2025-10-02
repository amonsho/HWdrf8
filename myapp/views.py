from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer,TaskSerializer, ProjectSerializer
from .permissions import IsAdmin, IsManagerOrAdmin, ViewOrChangeTask
from .models import CustomUser, Project, Task


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail":"Logout successfully"},status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"detail":"invalid token"},status=status.HTTP_400_BAD_REQUEST)
        
class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == CustomUser.ADMIN:
            return Project.objects.all()
        if user.role == CustomUser.MANAGER:
            return Project.objects.filter(owner=user)
        return Project.objects.all()
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.role in [CustomUser.ADMIN and CustomUser.MANAGER]:
            serializer.save(owner=user)

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsManagerOrAdmin]


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == CustomUser.ADMIN:
            return Task.objects.all()
        if user.role == CustomUser.MANAGER:
            return Task.objects.filter(project__owner=user)
        return Task.objects.filter(assigne=user)
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.role in [CustomUser.ADMIN and CustomUser.MANAGER]:
            serializer.save(assigne=user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, ViewOrChangeTask]
