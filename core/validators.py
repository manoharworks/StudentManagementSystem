from django.core.validators import RegexValidator

validate_phone = RegexValidator(
    regex=r"^\+?\d{10,15}$",
    message="Phone number must start with an optional '+' followed by 10 to 15 digits.",
)
