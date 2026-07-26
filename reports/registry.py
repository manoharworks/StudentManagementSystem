"""
Registry of all available reports.
"""

from dataclasses import dataclass

from attendance.models import Attendance
from courses.models import Course
from departments.models import Department
from enrollments.models import Enrollment
from grades.models import Grade
from students.models import Student

from reports.definitions import (
    AttendanceReport,
    CourseReport,
    DepartmentReport,
    EnrollmentReport,
    GradeReport,
    StudentReport,
)


@dataclass(frozen=True, slots=True)
class ReportConfig:
    """
    Configuration for a report.
    """

    model: type

    report: object

    select_related: tuple[str, ...] = ()


REPORTS = {
    "students": ReportConfig(
        model=Student,
        report=StudentReport,
        select_related=(
            "department",
        ),
    ),
    "departments": ReportConfig(
        model=Department,
        report=DepartmentReport,
    ),
    "courses": ReportConfig(
        model=Course,
        report=CourseReport,
        select_related=(
            "department",
        ),
    ),
    "enrollments": ReportConfig(
        model=Enrollment,
        report=EnrollmentReport,
        select_related=(
            "student",
            "course",
        ),
    ),
    "attendance": ReportConfig(
        model=Attendance,
        report=AttendanceReport,
        select_related=(
            "enrollment",
            "enrollment__student",
            "enrollment__course",
        ),
    ),
    "grades": ReportConfig(
        model=Grade,
        report=GradeReport,
        select_related=(
            "enrollment",
            "enrollment__student",
            "enrollment__course",
        ),
    ),
}