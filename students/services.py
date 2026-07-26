from .models import Student

SORT_OPTIONS = {
    "name": ("name", "id"),
    "-name": ("-name", "-id"),
    "department": ("department__name", "name"),
    "-department": ("-department__name", "-name"),
}

DEFAULT_SORT = "name"


class StudentService:
    """
    Business logic for Student.
    """

    @staticmethod
    def get_filtered_students(
        *,
        search="",
        department="",
        sort=DEFAULT_SORT,
    ):
        """
        Return a filtered queryset.
        """

        if sort not in SORT_OPTIONS:
            sort = DEFAULT_SORT

        return (
            Student.objects
            .with_department()
            .search(search)
            .filter_by_department(department)
            .order_by(*SORT_OPTIONS[sort])
        )

    @staticmethod
    def build_queryset_from_request(request):
        """
        Convert request parameters into a queryset.

        Used by HTML views, reports and APIs.
        """

        return StudentService.get_filtered_students(
            search=request.GET.get("q", ""),
            department=request.GET.get("department", "").strip(),
            sort=request.GET.get("sort", DEFAULT_SORT),
        )