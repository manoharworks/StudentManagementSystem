# departments/services.py

from .models import Department

SORT_OPTIONS = {
    "name": ("name",),
    "-name": ("-name",),
    "code": ("code",),
    "-code": ("-code",),
}

DEFAULT_SORT = "name"


class DepartmentService:
    """
    Business logic for departments.
    """

    @staticmethod
    def get_filtered_departments(
        *,
        search="",
        sort=DEFAULT_SORT,
    ):

        if sort not in SORT_OPTIONS:
            sort = DEFAULT_SORT

        return (
            Department.objects
            .search(search)
            .order_by(*SORT_OPTIONS[sort])
        )

    @staticmethod
    def build_queryset_from_request(request):

        return DepartmentService.get_filtered_departments(
            search=request.GET.get("q", ""),
            sort=request.GET.get("sort", DEFAULT_SORT),
        )