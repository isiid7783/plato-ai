import streamlit as st
from context_parser import parse_context
from decision_engine import decide, DECISION

st.set_page_config(page_title="Plato AI", layout="centered")

st.title("Plato AI")

user_input = st.text_area("Input", height=150)

if st.button("Run") and user_input.strip():
    ctx = parse_context(user_input)
    decision = decide(ctx)

    st.subheader("Decision")

    if decision == DECISION.REFUSE:
        st.error("REFUSE")

    elif decision == DECISION.DEFER:
        st.warning("DEFER")

    elif decision == DECISION.SILENCE:
        st.info("SILENCE")

    elif decision == DECISION.EXECUTE:
        st.success("EXECUTE")
      
