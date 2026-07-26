"""
Business logic for report exporting.
"""

from django.http import Http404

from reports.exporters.csv import CSVExporter
from reports.exporters.excel import ExcelExporter
from reports.exporters.pdf import PDFExporter


class ReportService:
    """
    Service responsible for exporting reports.
    """

    EXPORTERS = {
        "csv": CSVExporter,
        "excel": ExcelExporter,
        "pdf": PDFExporter,
    }

    @classmethod
    def export(
        cls,
        *,
        export_format,
        queryset,
        report,
    ):
        """
        Export a queryset using the requested format.

        Args:
            export_format:
                csv, excel or pdf.

            queryset:
                Django queryset.

            report:
                ReportDefinition instance.
        """

        exporter = cls.EXPORTERS.get(export_format)

        if exporter is None:
            raise Http404("Unsupported export format.")

        return exporter.export(
            queryset=queryset,
            report=report,
        )