"""
URL configuration for reports.
"""

from django.urls import path

from . import views

app_name = "reports"

urlpatterns = [
    path(
        "<str:report_name>/<str:export_format>/",
        views.export_report,
        name="export",
    ),
]