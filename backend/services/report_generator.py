from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    patient_notes,
    diagnosis,
    validation
):

    report_path = "orbit_report.pdf"

    doc = SimpleDocTemplate(
        report_path
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "ORBIT Medical Analysis Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"<b>Uploaded File:</b> {filename}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"<b>Patient Notes:</b> {patient_notes}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>Possible Conditions</b>",
            styles["Heading2"]
        )
    )

    for condition in diagnosis.get(
        "possible_conditions",
        []
    ):
        content.append(
            Paragraph(
                f"• {condition}",
                styles["BodyText"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>Clinical Evidence</b>",
            styles["Heading2"]
        )
    )

    for evidence in diagnosis.get(
        "evidence",
        []
    ):
        content.append(
            Paragraph(
                f"• {evidence}",
                styles["BodyText"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>Recommendations</b>",
            styles["Heading2"]
        )
    )

    for recommendation in diagnosis.get(
        "recommendations",
        []
    ):
        content.append(
            Paragraph(
                f"• {recommendation}",
                styles["BodyText"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>Validation Review</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            validation.get(
                "feedback",
                ""
            ),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>Disclaimer</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            "This report is AI-assisted and does not constitute a medical diagnosis. Consult a licensed healthcare professional.",
            styles["BodyText"]
        )
    )

    doc.build(content)

    return report_path