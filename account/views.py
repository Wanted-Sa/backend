
from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import APIException


from account.services import (
    AccountService
)
from account.serializers import (
    SignUpSerializer
)
from config.common.decorator import (
    required_data,
    optional_data,
)

class SingUpAPI(APIView):
    
    @required_data('email', 'password')
    def post(self, request, rd):
        try:
            account = AccountService.create_account(rd['email'], rd['password'])
        
        except ValueError as e:
            raise APIException(e.errors()[0]['msg'])
        
        except Exception as e:
            raise APIException(e)
        
        context = {
            'account': SignUpSerializer(account).data,
        }
        return JsonResponse(data=context, status=status.HTTP_201_CREATED)
            