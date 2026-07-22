from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings

from .forms import GradeForm
from .models import Grade

@login_required
def grade_list(request):

    queryset = (
        Grade.objects
        .select_related(
            "enrollment",
            "enrollment__student",
            "enrollment__course",
        )
        .order_by(
            "enrollment__student__name",
            "enrollment__course__title",
        )
    )

    search = request.GET.get("q", "").strip()

    result = request.GET.get("result", "").strip()

    if search:

        queryset = queryset.filter(

            Q(enrollment__student__name__icontains=search)

            |

            Q(enrollment__course__title__icontains=search)

        )

    if result:

        queryset = queryset.filter(result=result)

    paginator = Paginator(queryset, settings.ITEMS_PER_PAGE)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {

        "page_obj": page_obj,

        "search": search,

        "selected_result": result,

        "result_choices": Grade.Result.choices,

    }

    return render(
        request,
        "grades/grade_list.html",
        context,
    )


@login_required
def grade_create(request):

    if request.method == "POST":

        form = GradeForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Grade created successfully."
            )

            return redirect(
                "grades:grade_list"
            )

    else:

        form = GradeForm()

    return render(
        request,
        "grades/grade_form.html",
        {
            "form": form,
            "title": "Add Grade",
        },
    )


@login_required
def grade_detail(request, pk):

    grade = get_object_or_404(

        Grade.objects.select_related(
            "enrollment",
            "enrollment__student",
            "enrollment__course",
        ),

        pk=pk,
    )

    return render(

        request,

        "grades/grade_detail.html",

        {

            "grade": grade,

        }

    )


@login_required
def grade_update(request, pk):

    grade = get_object_or_404(
        Grade,
        pk=pk,
    )

    if request.method == "POST":

        form = GradeForm(
            request.POST,
            instance=grade,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Grade updated successfully."
            )

            return redirect(
                "grades:grade_detail",
                pk=grade.pk,
            )

    else:

        form = GradeForm(
            instance=grade,
        )

    return render(

        request,

        "grades/grade_form.html",

        {

            "form": form,

            "grade": grade,

            "title": "Update Grade",

        },

    )


@login_required
def grade_delete(request, pk):

    grade = get_object_or_404(
        Grade,
        pk=pk,
    )

    if request.method == "POST":

        grade.delete()

        messages.success(
            request,
            "Grade deleted successfully."
        )

        return redirect(
            "grades:grade_list"
        )

    return render(

        request,

        "grades/grade_confirm_delete.html",

        {

            "grade": grade,

        },

    )