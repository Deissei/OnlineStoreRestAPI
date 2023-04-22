from rest_framework.permissions import BasePermission

class IsManufacturer(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('POST', 'DELETE', 'UPDATE'):
            return True
        return bool(obj.manufacturer == request.user)
