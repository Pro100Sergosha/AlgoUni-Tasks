from django.urls import path
from .views import UserView, ParcelViewset, ChangeParcelViewset, DeliveryProofViewset, MarkAsDeliveredView, ListCourierParcels, TakeParcelViewset


urlpatterns = [
    path('users/', UserView.as_view()),
    path('parcels/', ParcelViewset.as_view()),
    path('parcels/<int:id>', ChangeParcelViewset.as_view()),
    path('take-parcel/<int:id>', TakeParcelViewset.as_view()),
    path('parcels/<int:id>/delivery_proof/', DeliveryProofViewset.as_view()),
    path('parcels/<int:id>/delivered/', MarkAsDeliveredView.as_view()),
    path('courier-parcels/', ListCourierParcels.as_view())
]
