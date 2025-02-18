from rest_framework import serializers
from .models import Task


class ToDoSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
    
    def get_email(self, obj):
        return obj.email.email