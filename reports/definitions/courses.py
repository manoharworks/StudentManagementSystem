"""
Course report definition.
"""

from reports.definitions.base import (
    ReportColumn,
    ReportDefinition,
)

CourseReport = ReportDefinition(
    title="Course Report",
    filename="courses",
    columns=[
        ReportColumn(
            header="Code",
            field="code",
        ),
        ReportColumn(
            header="Title",
            field="title",
        ),
        ReportColumn(
            header="Credits",
            field="credits",
        ),
        ReportColumn(
            header="Department",
            field="department__name",
        ),
    ],
)