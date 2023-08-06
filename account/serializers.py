from rest_framework.serializers import ModelSerializer

from account.models import Account


class SignUpSerializer(ModelSerializer):
    
    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'created_at',
            'updated_at',
        )
