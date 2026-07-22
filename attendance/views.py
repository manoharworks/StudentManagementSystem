from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings

from .forms import AttendanceForm
from .models import Attendance

@login_required
def attendance_list(request):

    queryset = (
        Attendance.objects
        .select_related(
            "enrollment",
            "enrollment__student",
            "enrollment__course",
        )
        .order_by("-date")
    )

    search = request.GET.get("q", "").strip()

    status = request.GET.get("status", "").strip()

    if search:

        queryset = queryset.filter(

            Q(enrollment__student__name__icontains=search)

            |

            Q(enrollment__course__title__icontains=search)

        )

    if status:

        queryset = queryset.filter(status=status)

    paginator = Paginator(queryset, settings.ITEMS_PER_PAGE)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {

        "page_obj": page_obj,

        "search": search,

        "selected_status": status,

        "status_choices": Attendance.Status.choices,

    }

    return render(
        request,
        "attendance/attendance_list.html",
        context,
    )


@login_required
def attendance_create(request):

    if request.method == "POST":

        form = AttendanceForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Attendance marked successfully."
            )

            return redirect(
                "attendance:attendance_list"
            )

    else:

        form = AttendanceForm()

    return render(
        request,
        "attendance/attendance_form.html",
        {
            "form": form,
            "title": "Mark Attendance",
        },
    )


@login_required
def attendance_detail(request, pk):

    attendance = get_object_or_404(

        Attendance.objects.select_related(
            "enrollment",
            "enrollment__student",
            "enrollment__course",
        ),

        pk=pk,
    )

    return render(

        request,

        "attendance/attendance_detail.html",

        {
            "attendance": attendance,
        },

    )


@login_required
def attendance_update(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk,
    )

    if request.method == "POST":

        form = AttendanceForm(
            request.POST,
            instance=attendance,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Attendance updated successfully."
            )

            return redirect(
                "attendance:attendance_detail",
                pk=attendance.pk,
            )

    else:

        form = AttendanceForm(
            instance=attendance
        )

    return render(

        request,

        "attendance/attendance_form.html",

        {

            "form": form,

            "title": "Update Attendance",

            "attendance": attendance,

        },

    )


@login_required
def attendance_delete(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk,
    )

    if request.method == "POST":

        attendance.delete()

        messages.success(
            request,
            "Attendance deleted successfully."
        )

        return redirect(
            "attendance:attendance_list"
        )

    return render(

        request,

        "attendance/attendance_confirm_delete.html",

        {
            "attendance": attendance,
        },

    )