from ..models import User
from .exceptions import UserAlreadyExistsError


def register_new_user(
    first_name: str,
    last_name: str,
    username: str,
    email: str,
    password: str,
) -> User:
    if User.objects.filter(email=email).exists():
        raise UserAlreadyExistsError()

    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=password,
    )

    return user


def set_user_permission_level(email: str, is_staff: bool) -> bool:
    result = User.objects.filter(email=email).update(is_staff=is_staff)
    return bool(result)
