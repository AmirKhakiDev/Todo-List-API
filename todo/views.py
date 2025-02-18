from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated

from todo.permission import IsUserIsobject

from .models import Task
from .serializers import ToDoSerializer


class ListTasks(GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsUserIsobject]

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CreateTask(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsUserIsobject]

    def perform_create(self, serializer):
        return serializer.save(email=self.request.user)
