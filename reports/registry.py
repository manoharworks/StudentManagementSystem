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
from students.services import StudentService


from reports.definitions import (
    AttendanceReport,
    CourseReport,
    DepartmentReport,
    EnrollmentReport,
    GradeReport,
    StudentReport,
)


from typing import Callable

@dataclass(frozen=True)
class ReportConfig:
    """
    Configuration for a report.
    """

    report: type

    queryset_provider: Callable


REPORTS = {

    "students": ReportConfig(
        report=StudentReport,
        queryset_provider=StudentService.build_queryset_from_request,
    ),
    
    # "courses": ReportConfig(
    #     report_class=CourseReport,
    #     queryset_provider=CourseService.build_queryset_from_request,
    # ),

    # "departments": ReportConfig(
    #     report_class=DepartmentReport,
    #     queryset_provider=DepartmentService.build_queryset_from_request,
    # ),

    # "enrollments": ReportConfig(
    #     report_class=EnrollmentReport,
    #     queryset_provider=EnrollmentService.build_queryset_from_request,
    # ),

    # "attendance": ReportConfig(
    #     report_class=AttendanceReport,
    #     queryset_provider=AttendanceService.build_queryset_from_request,
    # ),

    # "grades": ReportConfig(
    #     report_class=GradeReport,
    #     queryset_provider=GradeService.build_queryset_from_request,
    # ),
    
}