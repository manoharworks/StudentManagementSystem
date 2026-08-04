from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

from .services import StudentService, DEFAULT_SORT
from .models import Student
from .forms import StudentForm
from departments.models import Department

@permission_required("view_student", raise_exception=True)
@login_required
def student_list(request):

    queryset = StudentService.build_queryset_from_request(
        request
    )

    paginator = Paginator(
        queryset,
        settings.ITEMS_PER_PAGE,
    )

    page_obj = paginator.get_page(
        request.GET.get("page")
    )

    context = {
        "page_obj": page_obj,
        "search": request.GET.get("q", ""),
        "departments": Department.objects.order_by("name"),
        "selected_department": request.GET.get(
            "department",
            "",
        ),
        "sort": request.GET.get(
            "sort",
            DEFAULT_SORT,
        ),
    }

    return render(
        request,
        "students/student_list.html",
        context,
    )

@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, "Student created successfully.")

            return redirect("students:student_list")

    else:
        form = StudentForm()

    context = {
        "form": form,
    }

    return render(request, "students/student_form.html", context)


@login_required
def student_detail(request, pk):

    student = get_object_or_404(Student, pk=pk)

    context = {"student": student}

    return render(request, "students/student_detail.html", context)


@login_required
def student_update(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)

        if form.is_valid():
            form.save()

            messages.success(request, "Student detail updated successfully.")

            return redirect("students:student_detail", pk=student.pk)

    else:
        form = StudentForm(instance=student)

    context = {
        "form": form,
        "student": student,
    }

    return render(request, "students/student_form.html", context)


@login_required
def student_delete(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()

        messages.success(request, "Student deleted successfully.")
        return redirect("students:student_list")

    context = {"student": student}
    return render(request, "students/student_confirm_delete.html", context)
