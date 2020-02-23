from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import UserRole


def role_required(allowed_roles=[]):
    # pylint: disable=dangerous-default-value
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            user_role = get_object_or_404(UserRole, role_name=request.user.role)
            if user_role.role_number in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                print("hii", request.user.role)
                print(allowed_roles)
                raise PermissionDenied
        return wrap
    return decorator
