from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Parcel, DeliveryProof, CustomUser
from .serializers import ParcelSerializer, DeliveryProofSerializer, CustomUserSerializer
from .permissions import *


class UserView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        if request.user.is_authenticated and request.user.role == 'admin':
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.user.is_authenticated and not request.user.role == 'admin':
            user = CustomUserSerializer(request.user)
            return Response(user.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        


class ParcelViewset(APIView):
    permission_classes = [IsAuthenticated, CanCreateParcels]
    def get(self, request):
        if request.user.role == 'customer':
            user = CustomUser.objects.get(id=request.user.id)
            parcels = Parcel.objects.filter(sender_id=user.id)
            serializer = ParcelSerializer(parcels, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.user.role =='admin':
            parcels = Parcel.objects.all()
            serializer = ParcelSerializer(parcels, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
    def post(self, request):
        if request.user.role not in ['customer', 'admin']:
            return Response({'message': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ParcelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)