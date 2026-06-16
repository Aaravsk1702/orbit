THRESHOLD = 85


def threshold_agent(validation_result):

    confidence = validation_result.get("confidence", 0)

    if confidence >= THRESHOLD:
        return {
            "approved": True,
            "confidence": confidence
        }

    return {
        "approved": False,
        "feedback": validation_result.get(
            "feedback",
            "Need stronger evidence"
        )
    }