from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True, slots=True)
class ReportColumn:

    header: str

    field: str | None = None

    getter: Callable[[Any], Any] | None = None

    def __post_init__(self):

        has_field = self.field is not None
        has_getter = self.getter is not None

        if has_field == has_getter:
            raise ValueError(
                "Exactly one of 'field' or 'getter' must be provided."
            )


@dataclass(frozen=True, slots=True)
class ReportDefinition:

    title: str

    filename: str

    columns: list[ReportColumn]