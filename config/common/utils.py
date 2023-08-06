from rest_framework.exceptions import APIException

from config.common.exceptions import (
    RequiredDataException,
)


def get_required_key(request, name):
    try:
        if request.method == 'GET':
            data = request.GET[name]
        else:
            data = request.POST[name]
        if data in ["", None]:
            raise RequiredDataException(f'{name} is required')
    except:
        try:
            json_body = request.data
            data = json_body[name]
            if data in ["", None]:
                raise RequiredDataException(f'{name} is required')
        except:
            raise RequiredDataException(f'{name} is required')

    return data


def get_optional_key_and_val(request, name, default_value=''):
    try:
        if request.method == 'GET':
            data = request.GET[name]
        else:
            data = request.POST[name]
        if data in ["", None, 'null', 'undefined']:
            data = default_value
    except:
        try:
            json_body = request.data
            data = json_body[name]
            if data in ["", None, 'null', 'undefined']:
                data = default_value
        except:
            data = default_value
    return data