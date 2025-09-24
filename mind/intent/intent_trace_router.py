def route_by_intent(intent, pulse):
    if intent == "restore_alignment":
        return {"route": "governance"}
    elif intent == "recovery":
        return {"route": "state_recalibration"}
    elif intent == "stability":
        return {"route": "foresight"}
    return {"route": "expression"}
