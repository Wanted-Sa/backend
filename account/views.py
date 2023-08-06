from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from account.services import AccountService
from account.validators import AccountValidator
from account.serializers import SignUpSerializer

from config.common.decorator import (
    required_data,
    optional_data,
)
from config.common.exceptions import ValidationException


class SignUpAPI(APIView):
    permission_classes = [AllowAny]
    
    @required_data('email', 'password')
    def post(self, request, rd):
        try:
            account = AccountService.create_account(rd['email'], rd['password'])
        
        except ValueError as e:
            raise ValidationException(e.errors()[0]['msg'])
        
        except Exception as e:
            raise APIException(e)
        
        context = {
            'account': SignUpSerializer(account).data,
        }
        return Response(data=context, status=status.HTTP_201_CREATED)


class SignInAPI(TokenViewBase):
    permission_classes = [AllowAny]
    _serializer_class = api_settings.TOKEN_OBTAIN_SERIALIZER
    
    @required_data('email', 'password')
    def post(self, request, rd):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        try:
            AccountValidator(email=rd['email'], password=rd['password'])
            serializer.is_valid(raise_exception=True)
        
        except ValueError as e:
            raise ValidationException(e.errors()[0]['msg'])
        
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        context = {
            'access_token': serializer.validated_data['access'],
            'refresh_token': serializer.validated_data['refresh'],
        }
        return Response(data=context, status=status.HTTP_200_OK)
        