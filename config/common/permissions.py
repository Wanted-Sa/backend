from rest_framework import status
from rest_framework.permissions import BasePermission

from config.common.exceptions import GenericAPIException


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.owner == user:
            return True

        if user.is_authenticated or user.is_anonymous:
            response = {"detail": "You do not have permission to perform this action."}
            raise GenericAPIException(status_code=status.HTTP_403_FORBIDDEN, detail=response)