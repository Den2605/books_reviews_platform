import re

from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError(
            ("Год не может быть %(value)s больше текущего!"),
            params={"value": value},
        )


def validate_slug(slug):
    pattern = r"^[-a-zA-Z0-9_]+$"
    if not re.match(pattern, slug):
        raise ValidationError(
            "Разрешается использование только латинских букв "
            "(в верхнем и нижнем регистрах), цифр, дефисов и знака "
            'подчеркивания.", "@", "+", "-" и не содержать других символов.'
        )
