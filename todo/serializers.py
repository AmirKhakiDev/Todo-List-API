from rest_framework import serializers
from .models import Task


class ToDoSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_email(self, obj):
        return obj.email.email
    
