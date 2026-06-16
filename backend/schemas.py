from typing import TypedDict, List


class AgentState(TypedDict):

    report_text: str

    findings: List[str]

    possible_conditions: List[str]

    recommendations: List[str]

    confidence: int

    feedback: str

    approved: bool

    attempts: int