from django.db import transaction

from account.models import Account
from account.validators import AccountValidator


class AccountService:
    @transaction.atomic
    def create_account(email:str, password:str) -> Account:
        AccountValidator(email=email, password=password)
        account = Account.objects.create_user(email=email, password=password)
        return account
    