from rest_framework import permissions
from .models import CustomUser


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'customer'

class IsCourier(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'courier'

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class CanCreateParcels(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role in ['customer', 'admin']

class CanConfirmParcels(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role in ['customer', 'admin']


class CanChangeParcelStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role in ['courier', 'admin']

