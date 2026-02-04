from enum import Enum


class DECISION(Enum):
    EXECUTE = "EXECUTE"
    REFUSE = "REFUSE"
    DEFER = "DEFER"
    SILENCE = "SILENCE"


def decide(ctx):
    if ctx.get("responsibility_shift"):
        return DECISION.REFUSE

    if ctx.get("impulse"):
        return DECISION.REFUSE

    if not ctx.get("intent"):
        return DECISION.DEFER

    if ctx.get("silence"):
        return DECISION.SILENCE

    return DECISION.EXECUTE

