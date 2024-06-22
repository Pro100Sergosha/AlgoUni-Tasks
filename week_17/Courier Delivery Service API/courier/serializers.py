from rest_framework import serializers
from .models import *




class DeliveryProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryProof
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'role')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(password=password, **validated_data)
        return user
    

class ParcelSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializer(read_only=True)
    courier = CustomUserSerializer(read_only=True)
    delivery_proof = DeliveryProofSerializer(read_only=True)
    class Meta:
        model = Parcel
        fields = '__all__'
