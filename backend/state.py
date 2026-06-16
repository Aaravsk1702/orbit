from typing import TypedDict


class AgentState(TypedDict):
    report_text: str
    patient_notes: str

    diagnosis: dict
    validation: dict

    feedback: str

    approved: bool
    attempts: int