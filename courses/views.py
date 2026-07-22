from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings

from .models import Course
from .forms import CourseForm
from departments.models import Department

SORT_OPTIONS = {
    "semester": ("semester", "credit_hours"),
    "-semester": ("-semester", "-credit_hours"),
    "credit_hours": ("credit_hours", "semester"),
    "-credit_hours": ("-credit_hours", "-semester"),
}

DEFAULT_SORT = "semester"

def course_list(request):

    selected_department_id = request.GET.get("department", "").strip()
    search_query = request.GET.get("q", "")
    sort_key = request.GET.get("sort", DEFAULT_SORT)

    if sort_key not in SORT_OPTIONS:
        sort_key = DEFAULT_SORT

    queryset = Course.objects.select_related("department")

    if selected_department_id:
        queryset = queryset.filter(department_id=selected_department_id)

    if search_query:
        queryset = queryset.filter(
            Q(code__icontains=search_query) | Q(title__icontains=search_query)
        )

    if sort_key:
        queryset = queryset.order_by(*SORT_OPTIONS[sort_key])

    paginator = Paginator(queryset, settings.ITEMS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "search_query": search_query,
        "selected_department_id": selected_department_id,
        "departments": Department.objects.order_by("name"),
        "sort_key": sort_key,
    }

    return render(request, "courses/course_list.html", context)


def course_create(request):

    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Course created successfully")

            return redirect("courses:course_list")

    else:
        form = CourseForm()

    context = {
        "form": form,
        "title": "Add Course"
    }

    return render(request, "courses/course_form.html", context)


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {"course": course}

    return render(request, "courses/course_detail.html", context)


def course_update(request, pk):

    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)

        if form.is_valid():
            form.save()

            messages.success(request, "Course updated successfully")

            return redirect("courses:course_list")

    else:
        form = CourseForm(instance=course)

    context = {
        "form": form,
        "course": course,
        "title": "Update Course"
    }

    return render(request, "courses/course_form.html", context)


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course deleted successfully")
        return redirect("courses:course_list")

    context = {"course": course}
    return render(request, "courses/course_confirm_delete.html", context)
