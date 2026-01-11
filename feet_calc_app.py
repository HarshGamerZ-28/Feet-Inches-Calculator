import streamlit as st

st.set_page_config(page_title="Feet & Inches Calculator", layout="centered")

st.title("📏 Feet & Inches Calculator")

# -------------------------------
# Initialize session state safely
# -------------------------------
if "expr" not in st.session_state:
    st.session_state.expr = ""

# -------------------------------
# Input box
# -------------------------------
st.text_input(
    "Enter expression (example: 5'6\" + 3'4\")",
    key="expr"
)

# -------------------------------
# Buttons
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Calculate"):
        try:
            # Convert feet & inches to total inches
            import re

            def to_inches(match):
                feet = int(match.group(1))
                inches = int(match.group(2))
                return str(feet * 12 + inches)

            expr = st.session_state.expr

            # Replace 5'6" with inches
            expr = re.sub(r"(\d+)'\s*(\d+)\"", to_inches, expr)

            result_inches = eval(expr)

            feet = result_inches // 12
            inches = result_inches % 12

            st.success(f"Result: **{feet}' {inches}\"**")

        except Exception as e:
            st.error("Invalid expression ❌")

with col2:
    if st.button("Clear"):
        st.session_state.expr = ""

with col3:
    if st.button("Example"):
        st.session_state.expr = "5'6\" + 3'4\""

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Made with Streamlit ❤️")

