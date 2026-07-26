"""
Utility functions used by report exporters.
"""

from datetime import date, datetime
from decimal import Decimal

from django.db import models


def get_field_value(instance, field):

    value = instance

    current_model = instance.__class__

    field_parts = field.split("__")

    for index, attribute in enumerate(field_parts):

        is_last = index == len(field_parts) - 1

        if is_last:

            try:

                model_field = current_model._meta.get_field(attribute)

                if model_field.choices:

                    display_method = getattr(
                        value,
                        f"get_{attribute}_display",
                        None,
                    )

                    if callable(display_method):
                        return display_method()

            except models.FieldDoesNotExist:
                pass

        value = getattr(value, attribute)

        if value is None:
            return ""

        if hasattr(value, "_meta"):
            current_model = value.__class__

    return format_export_value(value)


def format_export_value(value):
  
    if value is None:
        return ""

    if isinstance(value, bool):
        return "Yes" if value else "No"

    if isinstance(value, Decimal):
        return f"{value:.2f}"

    if isinstance(value, datetime):
        return value.strftime("%d-%m-%Y %H:%M")

    if isinstance(value, date):
        return value.strftime("%d-%m-%Y")

    return str(value)