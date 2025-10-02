from django.urls import path
from .views import RegisterView, LogoutView, ProjectListCreateView,ProjectRetrieveUpdateDestroyView,TaskListCreateView,TaskRetrieveUpdateDestroyView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('projects/',ProjectListCreateView.as_view()),
    path('projects/<int:pk>',ProjectRetrieveUpdateDestroyView.as_view()),
    path('tasks/',TaskListCreateView.as_view()),
    path('tasks/<int:pk>',TaskRetrieveUpdateDestroyView.as_view())
]
