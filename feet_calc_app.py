import streamlit as st
import re

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Feet Calculator",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
.calc-display {
    width: 100%;
    background: black;
    color: white;
    padding: 18px;
    font-size: 30px;
    text-align: right;
    border-radius: 14px;
    margin-bottom: 15px;
    min-height: 70px;
}
.calc-row {
    display: flex;
    gap: 8px;
    margin-bottom: 8px;
}
.calc-row button {
    flex: 1;
    height: 65px;
    font-size: 24px;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

st.title("📏 Feet–Inch Calculator")

# -----------------------------
# Session state
# -----------------------------
if "display" not in st.session_state:
    st.session_state.display = ""

# -----------------------------
# Functions
# -----------------------------
def press(val):
    st.session_state.display += val

def delete():
    st.session_state.display = st.session_state.display[:-1]

def clear():
    st.session_state.display = ""

def feet_to_inches(num):
    if "." in num:
        f, i = num.split(".")
        return int(f) * 12 + int(i)
    return int(num) * 12

def calculate():
    try:
        expr = st.session_state.display
        expr = expr.replace("×", "*").replace("÷", "/")

        # Detect operation type
        if "*" in expr or "/" in expr:
            final_divisor = 144
        else:
            final_divisor = 12

        tokens = re.split(r'([+\-*/])', expr)
        converted = []

        for t in tokens:
            if t.isdigit() or "." in t:
                converted.append(str(feet_to_inches(t)))
            else:
                converted.append(t)

        inch_expr = "".join(converted)
        result_inches = eval(inch_expr)

        result = result_inches / final_divisor
        st.session_state.display = str(round(result, 2))

    except:
        st.session_state.display = "Error"

# -----------------------------
# Display
# -----------------------------
st.markdown(
    f"<div class='calc-display'>{st.session_state.display}</div>",
    unsafe_allow_html=True
)

# -----------------------------
# Buttons
# -----------------------------
rows = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["0", ".", "⌫", "+"],
]

for row in rows:
    st.markdown("<div class='calc-row'>", unsafe_allow_html=True)
    for btn in row:
        if btn == "⌫":
            st.button(btn, on_click=delete)
        elif btn == "−":
            st.button(btn, on_click=press, args=("-",))
        else:
            st.button(btn, on_click=press, args=(btn,))
    st.markdown("</div>", unsafe_allow_html=True)

st.button("C", use_container_width=True, on_click=clear)
st.button("=", use_container_width=True, on_click=calculate)

st.caption("➕➖ → ÷12   |   ✖➗ → ÷144")
