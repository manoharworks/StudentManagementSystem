from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from students.models import Student
from departments.models import Department


@login_required
def dashboard(request):

    total_students = Student.objects.count()

    total_departments = Department.objects.count()

    recent_students = Student.objects.select_related(
        "department"
    ).order_by("-id")[:5]

    context = {

        "total_students": total_students,

        "total_departments": total_departments,

        "recent_students": recent_students,

    }

    return render(

        request,

        "core/dashboard.html",

        context,

    )