from reports.definitions.base import (
    ReportColumn,
    ReportDefinition,
)

StudentReport = ReportDefinition(
    title="Student Report",
    filename="students",
    columns=[
        ReportColumn(
            header="Roll Number",
            field="roll_number",
        ),
        ReportColumn(
            header="Name",
            field="name",
        ),
        ReportColumn(
            header="Department",
            field="department__name",
        ),
        ReportColumn(
            header="Email",
            field="email",
        ),
        ReportColumn(
            header="Phone",
            field="phone",
        ),
        ReportColumn(
            header="Gender",
            field="gender",
        ),
        ReportColumn(
            header="Date of Birth",
            field="date_of_birth",
        ),
    ],
)