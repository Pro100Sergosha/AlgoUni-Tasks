from django.urls import path, include
from .views import UserView, ParcelViewset


urlpatterns = [
    path('users/', UserView.as_view()),
    path('parcels/', ParcelViewset.as_view())
]
