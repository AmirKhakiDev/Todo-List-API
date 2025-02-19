from rest_framework.routers import DefaultRouter
from .views import UserManagement
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserManagement, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]
