from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.conf import settings



from .models import Student
from .forms import StudentForm
from departments.models import Department

SORT_OPTIONS = {
    "name": ("name", "id"),
    "-name": ("-name", "-id"),
    "department": ("department__name", "name"),
    "-department": ("-department__name", "-name"),
}

DEFAULT_SORT = "name"


@login_required
def student_list(request):

    search_query = request.GET.get("q", "")
    selected_department_id = request.GET.get("department", "").strip()
    sort_key = request.GET.get("sort", DEFAULT_SORT)

    if sort_key not in SORT_OPTIONS:
        sort_key = DEFAULT_SORT

    queryset = (
        Student.objects.with_department()
        .search(search_query)
        .filter_by_department(selected_department_id)
    )
    
    # Sorting
    queryset = queryset.order_by(*SORT_OPTIONS[sort_key])

    # Pagination
    paginator = Paginator(queryset, settings.ITEMS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "search": search_query,
        "departments": Department.objects.order_by("name"),
        "selected_department": selected_department_id,
        "sort": sort_key,
    }

    return render(request, "students/student_list.html", context)


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
