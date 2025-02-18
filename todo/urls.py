from rest_framework.routers import DefaultRouter
from django.urls import *
from .views import ListTasks, CreateTask



urlpatterns = [
    path('tasks/', ListTasks.as_view(), name="task"),
    path('task/create/', CreateTask.as_view(), name='create'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]