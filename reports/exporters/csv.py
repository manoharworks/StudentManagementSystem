"""
Generic CSV exporter.
"""

import csv

from django.http import HttpResponse

from reports.utils import get_field_value


class CSVExporter:
    """
    Export any queryset to CSV using a ReportDefinition.
    """

    @staticmethod
    def export(*, queryset, report):
        """
        Export a queryset as a CSV file.

        Args:
            queryset:
                Django queryset to export.

            report:
                ReportDefinition instance describing the report.
        """

        response = HttpResponse(
            content_type="text/csv",
        )

        response["Content-Disposition"] = (
            f'attachment; filename="{report.filename}.csv"'
        )

        writer = csv.writer(response)

        # ----------------------------
        # Header Row
        # ----------------------------

        writer.writerow(
            [
                column.header
                for column in report.columns
            ]
        )

        # ----------------------------
        # Data Rows
        # ----------------------------

        for obj in queryset:

            row = []

            for column in report.columns:

                if column.getter is not None:

                    value = column.getter(obj)

                else:

                    value = get_field_value(
                        obj,
                        column.field,
                    )

                row.append(value)

            writer.writerow(row)

        return response