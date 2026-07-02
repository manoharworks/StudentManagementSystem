from django.urls import path
from .views import *

app_name = "students"

urlpatterns = [
    path("", student_list, name = "student_list"),
    path("add/", student_create, name = "student_create"),
    path ("<int:pk>/", student_detail, name = "student_detail" ),
    
]
