from rest_framework.routers import DefaultRouter
from django.urls import *
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView



urlpatterns = [
    path('', TaskListCreateView.as_view(), name="task"),
    path('<str:title>/',TaskRetrieveUpdateDeleteView.as_view(), name='option'),
]