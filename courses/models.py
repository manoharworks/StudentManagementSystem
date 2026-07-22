from django.db import models
from departments.models import Department

from core.models import TimeStampedModel

class Course(TimeStampedModel):
    
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

    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=50)
    credit_hours = models.PositiveSmallIntegerField(default=3)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name="courses"
    )
    semester = models.PositiveSmallIntegerField(
        blank=True, null=True, choices=SEMESTER_CHOICES
    )
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        ordering = ["semester", "code"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.code}-{self.title}"
