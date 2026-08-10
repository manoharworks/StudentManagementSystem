from django.urls import path
from .views import StudentListCreateAPIView, StudentDetailAPIView

app_name = "students_api"

urlpatterns = [
    path("students/", StudentListCreateAPIView.as_view(), name="student-list"),
    path("students/<int:pk>/", StudentDetailAPIView.as_view(), name="student-detail"),
    
]
