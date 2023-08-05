from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from account.manager import AccountManager


class Account(AbstractBaseUser):
    email = models.EmailField("이메일", max_length=255, unique=True, error_messages={"unique": "이미 사용중인 이메일 이거나 탈퇴한 이메일입니다."})
    password = models.CharField("비밀번호", max_length=128)
    is_admin = models.BooleanField("관리자 야부", default=False)
    is_active = models.BooleanField("로그인 여부", default=True)
    created_at = models.DateTimeField("계정 생성일", auto_now_add=True)
    updated_at = models.DateTimeField("계정 수정일", auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return f"[{self.id}][이메일]{self.email}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = "ACCOUNT"