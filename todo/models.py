from django.db import models
from account.models import User


class Task(models.Model):
    email  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userself")
    title = models.CharField(max_length=255, unique=True, primary_key=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
