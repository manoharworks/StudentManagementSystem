from rest_framework import serializers

from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        
        fields = [
                "roll_number",
                "name",
                "department",
                "email",
                "phone",
                "date_of_birth",
                "gender",
                "address",
                "photo",
            ]