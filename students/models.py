from django.db import models
from departments.models import Department

from core.managers import StudentManager
from core.validators import validate_phone
from core.mixins import TimeStampedMixin


class Student(TimeStampedMixin):
    
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
    ]

    objects = StudentManager()

    roll_number = models.CharField(
        max_length=20, 
        unique=True, null=True, 
        help_text="Unique roll no. of a student",
    )
    
    name = models.CharField(
        max_length=100
    )
    
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="students",
        blank=True,
        null=True,
    )
    
    email = models.EmailField(
        unique=True, 
        blank=True, 
        null=True)
    
    phone = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        validators=[validate_phone],
    )
    
    date_of_birth = models.DateField(
        blank=True, 
        null=True)
    
    gender = models.CharField(
        max_length=1, 
        blank=True, 
        null=True, 
        choices=GENDER_CHOICES
    )
    
    address = models.TextField(
        blank=True, 
        null=True)
    
    photo = models.ImageField(
        upload_to="students/", 
        blank=True, 
        null=True)

    class Meta:
        ordering = ["roll_number", "name"]

        # Used to improve the database query speed
        # Used only when both of the two conditions match:
        # 1) Fields having no unique=True or OneToOne Field, i.e avoid indexing if field attribute is set as unique=True
        # 2) Fields used in filtering, searching, or sorting
        # Note: Do not index columns with very low variety, such as a boolean field
        indexes = [models.Index(fields=["name"], name="student_name_index")]

    def __str__(self):
        return f"{self.name}"
