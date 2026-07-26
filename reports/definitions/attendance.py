"""
Attendance report definition.
"""

from reports.definitions.base import (
    ReportColumn,
    ReportDefinition,
)

AttendanceReport = ReportDefinition(
    title="Attendance Report",
    filename="attendance",
    columns=[
        ReportColumn(
            header="Student",
            field="enrollment__student__name",
        ),
        ReportColumn(
            header="Course",
            field="enrollment__course__title",
        ),
        ReportColumn(
            header="Date",
            field="date",
        ),
        ReportColumn(
            header="Status",
            field="status",
        ),
    ],
)