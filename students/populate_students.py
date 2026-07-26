from django.core.management.base import BaseCommand
from faker import Faker
from university.models import Student  # Replace with your model

class Command(BaseCommand):
    help = 'Generates dummy data for the University ERP'

    def handle(self, *args, **kwargs):
        faker = Faker()
        for _ in range(50):  # Creates 50 dummy students
            Student.objects.create(
                name=faker.name(),
                email=faker.email(),
                enrollment_id=faker.random_number(digits=6),
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated dummy data!'))
