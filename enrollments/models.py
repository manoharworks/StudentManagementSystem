from django.db import models
from students.models import Student
from courses.models import Course
class Enrollment(models.Model):
    SEMESTER_CHOICES = [
        (1, "Semester 1"),
        (2, "Semester 2"),
        (3, "Semester 3"),
        (4, "Semester 4"),
        (5, "Semester 5"),
        (6, "Semester 6"),
        (7, "Semester 7"),
        (8, "Semester 8"),
    ]

    """ 
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("COMPLETED", "Completed"),
        ("DROPPED", "Dropped"),
    ]
    """

    # Production Standard
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        COMPLETED = "COMPLETED", "Completed"
        DROPPED = "DROPPED", "Dropped"

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="enrollments"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="enrollments"
    )
    academic_year = models.CharField(
        max_length=9,
    )

    semester = models.PositiveSmallIntegerField(choices=SEMESTER_CHOICES)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    enrolled_at = models.DateField(
        auto_now_add=True,
    )

    class Meta:
        ordering = [
            "student",
            "course",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "student",
                    "course",
                    "academic_year",
                ],
                name="unique_student_course_year",
            )
        ]

    def __str__(self):

        return f"{self.student} → {self.course}"

    def total_classes(self):
        return self.attendance.count()

    def present_count(self):
        return self.attendance.filter(status="PRESENT").count()

    def absent_count(self):
        return self.attendance.filter(status="ABSENT").count()

    def late_count(self):
        return self.attendance.filter(status="LATE").count()

    def attendance_percentage(self):

        total = self.total_classes()

        if total == 0:
            return 0

        return round(
            (((self.present_count() + self.late_count()) / self.total_classes()) * 100),
            2,
        )
