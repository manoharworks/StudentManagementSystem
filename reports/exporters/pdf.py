"""
Generic PDF exporter.
"""

from io import BytesIO

from django.http import HttpResponse

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from reports.utils import get_field_value


class PDFExporter:
    """
    Export any queryset as a PDF document.
    """

    @staticmethod
    def export(*, queryset, report):

        buffer = BytesIO()

        document = SimpleDocTemplate(
            buffer,
            leftMargin=0.5 * inch,
            rightMargin=0.5 * inch,
            topMargin=0.5 * inch,
            bottomMargin=0.5 * inch,
        )

        styles = getSampleStyleSheet()

        title_style = styles["Heading1"]
        title_style.alignment = TA_CENTER

        elements = []

        # ---------------------------------
        # Report Title
        # ---------------------------------

        elements.append(
            Paragraph(
                report.title,
                title_style,
            )
        )

        elements.append(
            Spacer(
                1,
                0.3 * inch,
            )
        )

        # ---------------------------------
        # Table Data
        # ---------------------------------

        table_data = [
            [
                column.header
                for column in report.columns
            ]
        ]

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

            table_data.append(row)

        # ---------------------------------
        # Table
        # ---------------------------------

        table = Table(table_data)

        table.setStyle(
            TableStyle(
                [

                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#1F4E78"),
                    ),

                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.white,
                    ),

                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold",
                    ),

                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, 0),
                        10,
                    ),

                    (
                        "BACKGROUND",
                        (0, 1),
                        (-1, -1),
                        colors.whitesmoke,
                    ),

                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.grey,
                    ),

                    (
                        "ALIGN",
                        (0, 0),
                        (-1, -1),
                        "CENTER",
                    ),

                    (
                        "VALIGN",
                        (0, 0),
                        (-1, -1),
                        "MIDDLE",
                    ),

                ]
            )
        )

        elements.append(table)

        document.build(elements)

        pdf = buffer.getvalue()

        buffer.close()

        response = HttpResponse(
            pdf,
            content_type="application/pdf",
        )

        response["Content-Disposition"] = (
            f'attachment; filename="{report.filename}.pdf"'
        )

        return response