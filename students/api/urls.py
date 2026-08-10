from django.urls import path
from .views import StudentListAPIView

app_name = "students_api"

urlpatterns = [
    path("students/", StudentListAPIView.as_view(), name="list_student"),
]
