from rest_framework.permissions import BasePermission
from rest_framework.validators import ValidationError

class IsManufacturer(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('POST', 'DELETE', 'UPDATE'):
            return True
        return bool(obj.user_who == request.user)


class IsUserWho(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.user_who in ("ПОКУПАТЕЛЬ", ):
            raise ValidationError("Вы не продавец")
            