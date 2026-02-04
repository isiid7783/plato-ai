from decision_engine import decide, DECISION
from context_parser import parse_context


def test_responsibility_shift_refuse():
    ctx = parse_context("君が決めて")
    assert decide(ctx) == DECISION.REFUSE


def test_impulse_refuse():
    ctx = parse_context("今すぐ金を増やす方法を教えて")
    assert decide(ctx) == DECISION.REFUSE


def test_ambiguous_defer():
    ctx = parse_context("成功とは？")
    assert decide(ctx) == DECISION.DEFER


def test_silence():
    ctx = parse_context("言葉にした瞬間壊れる真理がある")
    assert decide(ctx) == DECISION.SILENCE


def test_execute_only_when_clear():
    ctx = parse_context("学習方法を教えて")
    assert decide(ctx) == DECISION.EXECUTE
