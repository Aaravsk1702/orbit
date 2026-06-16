from langgraph.graph import StateGraph, END

from backend.state import AgentState

from backend.agents.diagnosis import diagnosis_agent
from backend.agents.validation import validation_agent
from backend.agents.threshold import threshold_agent


def diagnosis_node(state: AgentState):

    diagnosis = diagnosis_agent(
        state["report_text"],
        state["patient_notes"],
        state.get("feedback", "")
    )

    state["diagnosis"] = diagnosis

    return state


def validation_node(state: AgentState):

    validation = validation_agent(
        state["report_text"],
        state["diagnosis"]
    )

    state["validation"] = validation

    return state


def threshold_node(state: AgentState):

    decision = threshold_agent(
        state["validation"]
    )

    print("\nThreshold Result:")
    print(decision)

    state["approved"] = decision["approved"]

    if not decision["approved"]:
        state["feedback"] = decision.get(
            "feedback",
            ""
        )

    state["attempts"] = state.get(
        "attempts",
        0
    ) + 1

    return state


def should_continue(state: AgentState):

    if state["approved"]:
        return END

    return END


workflow = StateGraph(AgentState)

workflow.add_node(
    "diagnosis",
    diagnosis_node
)

workflow.add_node(
    "validation",
    validation_node
)

workflow.add_node(
    "threshold",
    threshold_node
)

workflow.set_entry_point(
    "diagnosis"
)

workflow.add_edge(
    "diagnosis",
    "validation"
)

workflow.add_edge(
    "validation",
    "threshold"
)

workflow.add_conditional_edges(
    "threshold",
    should_continue
)

graph = workflow.compile()


def run_pipeline(
    report_text,
    patient_notes
):

    result = graph.invoke(
        {
            "report_text": report_text,
            "patient_notes": patient_notes,
            "feedback": "",
            "attempts": 0
        }
    )

    return {
        "approved": result["approved"],
        "attempts": result["attempts"],
        "diagnosis": result["diagnosis"],
        "validation": result["validation"]
    }