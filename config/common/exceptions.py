from rest_framework.exceptions import APIException


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code = status_code
        super().__init__(detail=detail, code=code)

class RequiredDataException(APIException):
    status_code = 400
    default_detail = 'Required data not found.'
    default_code = 'RequiredDataNotFound'
    

class ValidationException(APIException):
    status_code = 400
    default_detail = 'Validation failed.'
    default_code = 'ValidationFailed'