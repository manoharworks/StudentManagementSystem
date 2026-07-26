from django.db import models
from enrollments.models import Enrollment

from core.mixins import TimeStampedMixin

class Attendance(TimeStampedMixin):

    class Status(models.TextChoices):
        PRESENT = "PRESENT", "Present"
        ABSENT = "ABSENT", "Absent"
        LEFT = "LEFT", "Left"
        LATE = "LATE", "Late"

    enrollment = models.ForeignKey(
        Enrollment, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PRESENT)
    remarks = models.TextField(blank=True)
    class Meta:
        ordering = ["-date", "enrollment"]

        constraints = [models.UniqueConstraint(
            fields=["enrollment", "date"],
            name="Unique_enrollment_date",
        )
        ]

    def __str__(self):
        return f"{self.enrollment} - {self.status}"
