"""
Department report definition.
"""

from reports.definitions.base import (
    ReportColumn,
    ReportDefinition,
)

DepartmentReport = ReportDefinition(
    title="Department Report",
    filename="departments",
    columns=[
        ReportColumn(
            header="Code",
            field="code",
        ),
        ReportColumn(
            header="Department",
            field="name",
        ),
        ReportColumn(
            header="Description",
            field="description",
        ),
    ],
)