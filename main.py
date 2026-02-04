from decision_engine import decide, DECISION
from context_parser import parse_context


def run():
    text = input("Plato AI > ")

    ctx = parse_context(text)
    decision = decide(ctx)

    if decision == DECISION.REFUSE:
        print("[REFUSE]")

    elif decision == DECISION.DEFER:
        print("[DEFER]")

    elif decision == DECISION.SILENCE:
        pass

    else:
        print("[EXECUTE] LLM will be called here")


if __name__ == "__main__":
    run()
