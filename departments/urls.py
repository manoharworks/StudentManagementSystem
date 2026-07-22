from django.urls import path
from .views import (
    department_list,
    department_create,
    department_delete,
    department_detail,
    department_update,
)

app_name = "departments"

urlpatterns = [
    path("", department_list, name="department_list"),
    path("create/", department_create, name="department_create"),
    path("<int:pk>/", department_detail, name="department_detail"),
    path("<int:pk>/update/", department_update, name="department_update"),
    path("<int:pk>/delete/", department_delete, name="department_delete"),
]
