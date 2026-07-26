"""
Enrollment report definition.
"""

from reports.definitions.base import (
    ReportColumn,
    ReportDefinition,
)

EnrollmentReport = ReportDefinition(
    title="Enrollment Report",
    filename="enrollments",
    columns=[
        ReportColumn(
            header="Student",
            field="student__name",
        ),
        ReportColumn(
            header="Course",
            field="course__title",
        ),
        ReportColumn(
            header="Academic Year",
            field="academic_year",
        ),
        ReportColumn(
            header="Semester",
            field="semester",
        ),
        ReportColumn(
            header="Status",
            field="status",
        ),
        ReportColumn(
            header="Attendance %",
            getter=lambda enrollment: enrollment.attendance_percentage(),
        ),
    ],
)