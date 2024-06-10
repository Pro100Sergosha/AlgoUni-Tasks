from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParcelViewset

router = DefaultRouter()
router.register(r'parcels', ParcelViewset)

urlpatterns = [
    path('', include(router.urls))
]
