from rest_framework.routers import DefaultRouter
from .views import UserMnagement
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserMnagement, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]