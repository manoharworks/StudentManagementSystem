from django.db import models
from django.core.exceptions import ValidationError
from decimal import Decimal

from enrollments.models import Enrollment
from core.mixins import TimeStampedMixin


class Grade(TimeStampedMixin):
    class Result(models.TextChoices):
        PASS = "PASS", "Pass"
        FAIL = "FAIL", "Fail"

    GRADING_SCALE = (
        (90, "A+", Decimal("4.00"), Result.PASS),
        (80, "A",  Decimal("3.70"), Result.PASS),
        (70, "B+", Decimal("3.30"), Result.PASS),
        (60, "B",  Decimal("3.00"), Result.PASS),
        (50, "C",  Decimal("2.70"), Result.PASS),
        (40, "D",  Decimal("2.00"), Result.PASS),
        (0,  "F",  Decimal("0.00"), Result.FAIL),
    )

    enrollment = models.OneToOneField(
        Enrollment, on_delete=models.CASCADE, related_name="grade"
    )
    marks_obtained = models.DecimalField(
        decimal_places=2,
        max_digits=5,
    )
    maximum_marks = models.DecimalField(decimal_places=2, max_digits=5, default=100.00)
    percentage = models.DecimalField(decimal_places=2, max_digits=5, editable=False)
    letter_grade = models.CharField(max_length=2, editable=False)
    grade_point = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    result = models.CharField(max_length=5, choices=Result.choices, editable=False)
    remarks = models.TextField(blank=True)
    class Meta:
        
        ordering = ["enrollment"]
        
        constraints = [
            models.CheckConstraint(
                condition=models.Q(maximum_marks__gt=0),
                name="grade_maximum_marks_positive",
            ),
            models.CheckConstraint(
                condition=models.Q(marks_obtained__gte=0),
                name="grade_marks_obtained_non_negative",
            ),
            models.CheckConstraint(
                condition=models.Q(marks_obtained__lte=models.F("maximum_marks")),
                name="grade_marks_cannot_exceed_max",
            ),
        ]

    def __str__(self):
        return f"{self.enrollment.student}-{self.enrollment.course}"

    # Validation
    def clean(self):

        if self.maximum_marks <= 0:
            raise ValidationError("Maximum marks must be greater than zero.")

        if self.marks_obtained < 0:
            raise ValidationError("Marks cannot be negative.")

        if self.marks_obtained > self.maximum_marks:
            raise ValidationError("Marks obtained cannot exceed maximum marks.")

    def calculate_percentage(self):
        return round(((self.marks_obtained / self.maximum_marks) * 100), 2)

    def calculate_grade(self):

        percentage = self.calculate_percentage()

        for min_per, letter, point, status in self.GRADING_SCALE:
            if percentage >= min_per:
                return letter, point, status

    def save(self, *args, **kwargs):
        self.full_clean()

        self.percentage = self.calculate_percentage()
        self.letter_grade, self.grade_point, self.result = self.calculate_grade()

        super().save(*args, **kwargs)
