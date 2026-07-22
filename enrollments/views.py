from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings
from .models import Enrollment
from .forms import EnrollmentForm

def enrollment_list(request):

    selected_enrollment_status = request.GET.get("enrollment_status", "").strip()
    search_query = request.GET.get("q", "")

    queryset = Enrollment.objects.select_related("student", "course").order_by(
        "student__name", "course__code"
    )

    if selected_enrollment_status:
        queryset = queryset.filter(status=selected_enrollment_status)

    if search_query:
        queryset = queryset.filter(
            Q(student__name__icontains=search_query)
            | Q(student__roll_number__icontains=search_query)
            | Q(course__code__icontains=search_query)
            | Q(course__title__icontains=search_query)
        )

    paginator = Paginator(queryset, settings.ITEMS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "search_query": search_query,
        "selected_enrollment_status": selected_enrollment_status,
        "Status_Choices": Enrollment.Status.choices,
    }

    return render(request, "enrollments/enrollment_list.html", context)


def enrollment_create(request):

    if request.method == "POST":
        form = EnrollmentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment created successfully")

            return redirect("enrollments:enrollment_list")

    else:
        form = EnrollmentForm()

    context = {"form": form, "title": "Add Enrollment"}

    return render(request, "enrollments/enrollment_form.html", context)


def enrollment_detail(request, pk):
    enrollment = get_object_or_404(
        Enrollment.objects.select_related("student", "course"), pk=pk
    )
    context = {"enrollment": enrollment}

    return render(request, "enrollments/enrollment_detail.html", context)


def enrollment_update(request, pk):

    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == "POST":
        form = EnrollmentForm(request.POST, instance=enrollment)

        if form.is_valid():
            form.save()

            messages.success(request, "Enrollment updated successfully")

            return redirect("enrollments:enrollment_list")

    else:
        form = EnrollmentForm(instance=enrollment)

    context = {"form": form, "enrollment": enrollment, "title": "Update Enrollment"}

    return render(request, "enrollments/enrollment_form.html", context)


def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == "POST":
        enrollment.delete()
        messages.success(request, "Enrollment deleted successfully")
        return redirect("enrollments:enrollment_list")

    context = {"enrollment": enrollment}
    return render(request, "enrollments/enrollment_confirm_delete.html", context)
