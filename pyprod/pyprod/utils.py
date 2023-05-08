import os
from typing import Any

from django.core.exceptions import ImproperlyConfigured


class DefaultValue:
    pass


def get_env_variable(var_name: str, default: Any = DefaultValue, coerce_type: type = str):
    if coerce_type is bool:
        coerce_type = lambda value: value.lower() in {"1", "yes", "true", "on"}

    try:
        return coerce_type(os.environ[var_name])
    except (KeyError, ValueError):
        if default is not DefaultValue:
            return default
        raise ImproperlyConfigured(f"Set the {var_name} env variable")
