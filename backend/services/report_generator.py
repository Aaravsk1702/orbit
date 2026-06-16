from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_report(data, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Medical Assessment Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Possible Condition: {data['diagnosis']['possible_condition']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Recommendation: {data['diagnosis']['recommendation']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Confidence: {data['validation']['confidence']}%",
            styles["BodyText"]
        )
    )

    doc.build(content)

    return filename