from backend.agents.diagnosis import diagnosis_agent
from backend.agents.validation import validation_agent
from backend.agents.threshold import threshold_agent

MAX_ITERATIONS = 1


def run_pipeline(report_text, patient_notes):

    feedback = ""

    for attempt in range(MAX_ITERATIONS):

        diagnosis = diagnosis_agent(
            report_text,
            patient_notes,
            feedback
        )

        validation = validation_agent(
            report_text,
            diagnosis
        )

        decision = threshold_agent(
            validation
        )

        print("\nThreshold Result:")
        print(decision)

        if decision["approved"]:

            return {
                "approved": True,
                "attempts": attempt + 1,
                "diagnosis": diagnosis,
                "validation": validation
            }

        feedback = decision["feedback"]

    return {
        "approved": False,
        "attempts": MAX_ITERATIONS,
        "diagnosis": diagnosis,
        "validation": validation
    }