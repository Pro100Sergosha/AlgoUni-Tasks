from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewset

router = DefaultRouter()
router.register(r'blogs', BlogViewset)

urlpatterns = [
    path('', include(router.urls))    
]
