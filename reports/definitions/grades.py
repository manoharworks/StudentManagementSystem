"""
Grade report definition.
"""

from reports.definitions.base import (
    ReportColumn,
    ReportDefinition,
)

GradeReport = ReportDefinition(
    title="Grade Report",
    filename="grades",
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
            header="Marks",
            field="marks_obtained",
        ),
        ReportColumn(
            header="Maximum Marks",
            field="maximum_marks",
        ),
        ReportColumn(
            header="Percentage",
            field="percentage",
        ),
        ReportColumn(
            header="Letter Grade",
            field="letter_grade",
        ),
        ReportColumn(
            header="Grade Point",
            field="grade_point",
        ),
        ReportColumn(
            header="Result",
            field="result",
        ),
    ],
)