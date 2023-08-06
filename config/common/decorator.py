from functools import wraps

from config.common.utils import (
    get_optional_key_and_val,
    get_required_key,
)


def optional_data(*keys):
    def decorate(func):
        @wraps(func)
        def wrapper(View, *args, **kwargs):
            optional_data = dict()
            for arg in keys:
                for key, val in arg.items():
                    data = get_optional_key_and_val(View.request, key, val)
                    optional_data[key] = data
            return func(View, od=optional_data, *args, **kwargs)

        return wrapper

    return decorate


def required_data(*keys):
    def decorate(func):
        @wraps(func)
        def wrapper(View, *args, **kwargs):
            required_data = dict()
            for key in keys:
                data = get_required_key(View.request, key)
                required_data[key] = data
            return func(View, rd=required_data, *args, **kwargs)

        return wrapper

    return decorate