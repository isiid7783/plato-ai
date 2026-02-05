from enum import Enum
from typing import Dict


# =========================
# ENUMS
# =========================

class DECISION(Enum):
    EXECUTE = "EXECUTE"
    DEFER = "DEFER"
    REFUSE = "REFUSE"
    SILENCE = "SILENCE"


class QUESTION_GENRE(Enum):
    EXPLAIN = "EXPLAIN"       # A
    STRUCTURE = "STRUCTURE"   # B
    COMPARE = "COMPARE"       # C
    DEFINE = "DEFINE"         # D
    THINK = "THINK"           # E
    META = "META"             # F
    UNKNOWN = "UNKNOWN"


# =========================
# ENTRY POINT
# =========================

def generate_response(decision: DECISION, ctx: Dict[str, bool], text: str) -> str:
    if decision != DECISION.EXECUTE:
        return _respond_non_execute(decision)

    genre = detect_question_genre(text)

    if genre == QUESTION_GENRE.EXPLAIN:
        return respond_explain()

    if genre == QUESTION_GENRE.STRUCTURE:
        return respond_structure()

    if genre == QUESTION_GENRE.COMPARE:
        return respond_compare()

    if genre == QUESTION_GENRE.DEFINE:
        return respond_define()

    if genre == QUESTION_GENRE.THINK:
        return respond_think()

    if genre == QUESTION_GENRE.META:
        return respond_meta()

    return respond_unknown_execute()


# =========================
# GENRE DETECTION
# =========================

def detect_question_genre(text: str) -> QUESTION_GENRE:
    t = text.lower()

    if any(w in t for w in ["explain", "how does", "why does", "mechanism"]):
        return QUESTION_GENRE.EXPLAIN

    if any(w in t for w in ["organize", "structure", "break down", "clarify structure"]):
        return QUESTION_GENRE.STRUCTURE

    if any(w in t for w in ["compare", "difference", "vs", "pros and cons"]):
        return QUESTION_GENRE.COMPARE

    if any(w in t for w in ["define", "what is", "boundary", "scope"]):
        return QUESTION_GENRE.DEFINE

    if any(w in t for w in ["how should i think", "how to think", "consider", "reflect"]):
        return QUESTION_GENRE.THINK

    if any(w in t for w in ["is this question", "is this a valid question", "what is missing"]):
        return QUESTION_GENRE.META

    return QUESTION_GENRE.UNKNOWN


# =========================
# A. EXPLANATION REQUEST
# =========================

def respond_explain() -> str:
    return (
        "This question requests an explanation.\n\n"
        "A responsible explanation focuses on clarifying structure, mechanisms, "
        "and underlying assumptions, rather than offering directives or conclusions.\n\n"
        "Key elements are identified, their relationships are described, "
        "and the limits of what can be confidently stated are made explicit."
    )


# =========================
# B. STRUCTURE / ORGANIZATION
# =========================

def respond_structure() -> str:
    return (
        "This question requests structural clarification.\n\n"
        "A responsible response separates the subject into distinct elements, "
        "identifies how they relate to one another, and makes explicit where "
        "different levels or categories are being conflated.\n\n"
        "The aim is not to prioritize or conclude, but to reduce confusion "
        "by mapping the structure of the issue."
    )


# =========================
# C. COMPARISON
# =========================

def respond_compare() -> str:
    return (
        "This question requests a comparison.\n\n"
        "A valid comparison requires clearly defined criteria, shared dimensions, "
        "and awareness of contextual differences between the items being compared.\n\n"
        "Without explicit criteria, comparison risks becoming rhetorical rather "
        "than analytical."
    )


# =========================
# D. DEFINITION / BOUNDARY
# =========================

def respond_define() -> str:
    return (
        "This question requests a definition or boundary clarification.\n\n"
        "Definitions function by inclusion and exclusion. "
        "Clarifying what falls outside a concept is as important as stating what falls within it.\n\n"
        "Boundary-setting reduces ambiguity and prevents category errors."
    )


# =========================
# E. THINKING SUPPORT
# =========================

def respond_think() -> str:
    return (
        "This question seeks support for thinking rather than a direct answer.\n\n"
        "A responsible response surfaces assumptions, identifies constraints, "
        "and slows premature closure.\n\n"
        "Thinking is treated here as an ongoing process, not as a conclusion "
        "to be delivered."
    )


# =========================
# F. META-QUESTION
# =========================

def respond_meta() -> str:
    return (
        "This is a meta-level question about the question itself.\n\n"
        "Evaluating a question involves examining intent, scope, assumptions, "
        "and whether answering it would meaningfully reduce uncertainty.\n\n"
        "A question is considered valid when it can support a responsible response."
    )


# =========================
# UNKNOWN EXECUTE
# =========================

def respond_unknown_execute() -> str:
    return (
        "This question has been judged answerable, "
        "but its structure does not clearly match a predefined question type.\n\n"
        "A minimal explanatory response is therefore provided."
    )


# =========================
# NON-EXECUTE RESPONSES
# =========================

def _respond_non_execute(decision: DECISION) -> str:
    if decision == DECISION.DEFER:
        return "This question is deferred due to structural ambiguity."
    if decision == DECISION.REFUSE:
        return "This question is refused due to responsibility or ethical boundaries."
    if decision == DECISION.SILENCE:
        return ""
    return ""
  
