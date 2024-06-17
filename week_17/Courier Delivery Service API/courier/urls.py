from django.urls import path
from .views import UserView, ParcelViewset, ChangeParcelViewset, DeliveryProofViewset, MarkAsDeliveredView, ListCourierParcels, TakeParcelViewset


urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('parcels/', ParcelViewset.as_view(), name='parcels'),
    path('parcels/<int:id>', ChangeParcelViewset.as_view(), name='edit-parcel'),
    path('take-parcel/<int:id>', TakeParcelViewset.as_view(), name='take-parcel'),
    path('parcels/<int:id>/delivery_proof/', DeliveryProofViewset.as_view(), name='delivery-proof'),
    path('parcels/<int:id>/delivered/', MarkAsDeliveredView.as_view(), name='mark-as-delivered'),
    path('courier-parcels/', ListCourierParcels.as_view(), name='courier-parcels')
]
