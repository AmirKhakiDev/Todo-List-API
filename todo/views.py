from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from todo.permission import IsAuthenticatedAndOwner
from .models import Task
from .serializers import ToDoSerializer


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticatedAndOwner]

    # def get_queryset(self):
    #     return Task.objects.filter(email=self.request.user)

    def perform_create(self, serializer):
        serializer.save(email=self.request.user)


class TaskRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticatedAndOwner]
    lookup_field = "title"
    lookup_url_kwarg = "title"

    # def get_queryset(self):
    #     return Task.objects.filter(email=self.request.user)
