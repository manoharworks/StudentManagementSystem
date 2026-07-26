from django.db.models import Avg, Count

from attendance.models import Attendance
from courses.models import Course
from departments.models import Department
from enrollments.models import Enrollment
from grades.models import Grade
from students.models import Student


class DashboardService:

    @staticmethod
    def get_summary_data():
        return {
            "total_students": Student.objects.count(),
            "total_departments": Department.objects.count(),
            "total_courses": Course.objects.count(),
            "total_enrollments": Enrollment.objects.count(),
            "total_attendance": Attendance.objects.count(),
            "total_grades": Grade.objects.count(),
        }

    @staticmethod
    def get_attendance_statistics():
        total_attendance = Attendance.objects.count()

        present_count = Attendance.objects.filter(
            status=Attendance.Status.PRESENT
        ).count()

        absent_count = Attendance.objects.filter(
            status=Attendance.Status.ABSENT
        ).count()

        late_count = Attendance.objects.filter(
            status=Attendance.Status.LATE
        ).count()

        left_count = Attendance.objects.filter(
            status=Attendance.Status.LEFT
        ).count()

        attendance_percentage = (
            round(
                ((present_count + late_count) / total_attendance) * 100,
                2,
            )
            if total_attendance
            else 0
        )

        return {
            "present_count": present_count,
            "absent_count": absent_count,
            "late_count": late_count,
            "left_count": left_count,
            "attendance_percentage": attendance_percentage,
        }

    @staticmethod
    def get_grade_statistics():
        average_gpa = Grade.objects.aggregate(
            average_gpa=Avg("grade_point")
        )["average_gpa"]

        grade_distribution = (
            Grade.objects.values("letter_grade")
            .annotate(total=Count("id"))
            .order_by("letter_grade")
        )

        return {
            "average_gpa": average_gpa,
            "grade_distribution": grade_distribution,
        }

    @staticmethod
    def get_top_departments():
        return (
            Department.objects.annotate(
                student_count=Count("students")
            )
            .order_by("-student_count", "name")[:5]
        )

    @staticmethod
    def get_top_courses():
        return (
            Course.objects.annotate(
                enrollment_count=Count("enrollments")
            )
            .order_by("-enrollment_count", "code")[:5]
        )

    @staticmethod
    def get_recent_students():
        return (
            Student.objects.select_related("department")
            .order_by("-created_at")[:5]
        )

    @staticmethod
    def get_recent_enrollments():
        return (
            Enrollment.objects.select_related(
                "student",
                "course",
            )
            .order_by("-enrolled_at")[:5]
        )

    @staticmethod
    def get_recent_grades():
        return (
            Grade.objects.select_related(
                "enrollment",
                "enrollment__student",
                "enrollment__course",
            )
            .order_by("-created_at")[:5]
        )

    @classmethod
    def get_dashboard_data(cls):
        
        # Combine all dashboard information into one dictionary.

        context = {}

        context.update(cls.get_summary_data())
        context.update(cls.get_attendance_statistics())
        context.update(cls.get_grade_statistics())

        context["top_departments"] = cls.get_top_departments()
        context["top_courses"] = cls.get_top_courses()

        context["recent_students"] = cls.get_recent_students()
        context["recent_enrollments"] = cls.get_recent_enrollments()
        context["recent_grades"] = cls.get_recent_grades()

        return context