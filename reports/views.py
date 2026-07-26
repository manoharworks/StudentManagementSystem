"""
Views for exporting reports.
"""

from django.http import Http404

from reports.registry import REPORTS
from reports.services import ReportService


def export_report(
    request,
    report_name,
    export_format,
):
    """
    Export any registered report.
    """

    config = REPORTS.get(report_name)

    if config is None:
        raise Http404("Unknown report.")

    queryset = config.model.objects.all()

    if config.select_related:

        queryset = queryset.select_related(
            *config.select_related
        )

    return ReportService.export(
        export_format=export_format,
        queryset=queryset,
        report=config.report,
    )