from rest_framework import serializers

from apps.users.models import StoreUser


class StoreUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreUser
        fields = ('username', 'phone_number', 'user_who', 'password')
