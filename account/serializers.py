from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from account.models import Account


class SignUpSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'password',
            'created_at',
            'updated_at',
        )
