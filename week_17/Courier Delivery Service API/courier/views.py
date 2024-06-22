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


class ChangeParcelViewset(APIView):
    permission_classes = [IsAuthenticated, CanChangeParcelStatus, CanCreateParcels]
    def get(self, request, id):
        try:
            parcel = Parcel.objects.get(id=id)
            if not parcel.sender.id == request.user.id or request.user.role == 'admin':
                return Response({'message': 'No access for someone else\'s parcel'}, status=status.HTTP_403_FORBIDDEN)
        except Parcel.DoesNotExist:
            return Response({'message': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)
        if request.user.role in ['customer', 'admin']:
            serializer = ParcelSerializer(parcel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
        
    def put(self, request, id):
        try:
            parcel = Parcel.objects.get(id=id)
            if not parcel.sender.id == request.user.id or request.user.role == 'admin':
                return Response({'message': 'No access for someone else\'s parcel'}, status=status.HTTP_403_FORBIDDEN)
        except Parcel.DoesNotExist:
            return Response({'message': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user.role in ['customer', 'admin']:
            serializer = ParcelSerializer(parcel, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(courier = parcel.courier)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            parcel = Parcel.objects.get(id=id)
            if not parcel.sender.id == request.user.id or request.user.role == 'admin':
                return Response({'message': 'No access for someone else\'s parcel'}, status=status.HTTP_403_FORBIDDEN)
        except Parcel.DoesNotExist:
            return Response({'message': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user.role in ['customer', 'admin']:
            parcel.delete()
            return Response({'message': 'Parcel Deleted Successfuly'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)


class TakeParcelViewset(APIView):
    def get(self, request, id):
        try:
            parcel = Parcel.objects.get(id=id)
        except Parcel.DoesNotExist:
            return Response({'message': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)
        if request.user.role == 'courier' and parcel.status not in ['In Transit', 'Delivered']:
            serializer = ParcelSerializer(parcel, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(courier = request.user, status='In Transit')
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif not request.user.role == 'courier':
            return Response({'message': 'Not Allowed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Parcel already taken or delivered'}, status=status.HTTP_400_BAD_REQUEST)


class DeliveryProofViewset(APIView):
    permission_classes = [IsAuthenticated, CanChangeParcelStatus]
    def post(self, request, id):
        try:
            parcel = Parcel.objects.get(id=id)
            if not parcel.sender.id == request.user.id and not request.user.role in ['courier', 'admin']:
                return Response({'message': 'No access for someone else\'s parcel'}, status=status.HTTP_403_FORBIDDEN)
        except Parcel.DoesNotExist:
            return Response({'message': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)
        if not parcel.delivery_proof and request.user.role in ['courier', 'admin'] and parcel.courier == request.user:
            serializer = DeliveryProofSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                delivery_proof = DeliveryProof.objects.get(id = serializer.data['id'])
                parcel_serializer = ParcelSerializer(parcel, data=request.data, partial=True)
                if parcel_serializer.is_valid():
                    parcel_serializer.save(delivery_proof=delivery_proof)
                return Response(parcel_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
        elif not request.user.role in ['courier', 'admin'] or not parcel.courier == request.user:
            return Response({'message': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'message': 'This parcel already has delivery proof image'}, status=status.HTTP_400_BAD_REQUEST)


class MarkAsDeliveredView(APIView):
    def put(self, request, id):
        try:
            parcel = Parcel.objects.get(id=id)
            if not parcel.sender.id == request.user.id:
                return Response({'message': 'No access for someone else\'s parcel'}, status=status.HTTP_403_FORBIDDEN)
        except Parcel.DoesNotExist:
            return Response({'message': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)
        if parcel.delivery_proof and request.user.role in ['customer', 'admin']:
            serializer = ParcelSerializer(parcel, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(status='delivered')
                return Response(serializer.data, status=status.HTTP_200_OK)


class ListCourierParcels(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.role == 'courier':
            parcels = Parcel.objects.filter(courier=request.user)
            serializer = ParcelSerializer(parcels, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.user.role == 'admin':
            parcels = Parcel.objects.filter(courier__isnull=False)
            serializer = ParcelSerializer(parcels, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)