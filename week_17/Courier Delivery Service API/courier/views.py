from rest_framework.viewsets import ModelViewSet
from .models import Parcel, DeliveryProof, CustomUser
from .serializers import ParcelSerializer, DeliveryProofSerializer

class ParcelViewset(ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


    