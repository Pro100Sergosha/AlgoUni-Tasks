from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('courier', 'Courier'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=8, choices=ROLE_CHOICES, default='Customer')

class DeliveryProof(models.Model):
    image = models.ImageField(upload_to='delivery_proofs/')
    timestamp = models.DateTimeField(auto_now_add=True)

class Parcel(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    )
    title = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender', null=True, blank=True)
    receiver_name = models.CharField(max_length=40)
    receiver_address = models.TextField()
    courier = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='courier_parcels', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(null=True)
    delivery_proof = models.OneToOneField(DeliveryProof, on_delete=models.CASCADE, null=True)


