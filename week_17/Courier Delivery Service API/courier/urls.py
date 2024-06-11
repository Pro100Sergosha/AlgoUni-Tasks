from django.urls import path, include
from .views import UserView, ParcelViewset, ChangeParcelViewset, DeliveryProofViewset


urlpatterns = [
    path('users/', UserView.as_view()),
    path('parcels/', ParcelViewset.as_view()),
    path('parcels/<int:id>', ChangeParcelViewset.as_view()),
    path('parcels/<int:id>/delivery_proof/', DeliveryProofViewset.as_view())
]
