import streamlit as st

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Feet Calculator",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# Custom CSS (mobile friendly)
# -----------------------------
st.markdown("""
<style>
.display input {
    font-size: 28px !important;
    text-align: right;
    height: 70px;
}
.stButton > button {
    height: 65px;
    font-size: 24px;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

st.title("📏 Feet–Inch Calculator")

# -----------------------------
# Session State
# -----------------------------
if "display" not in st.session_state:
    st.session_state.display = ""

# -----------------------------
# Functions
# -----------------------------
def press(value):
    st.session_state.display += value

def clear():
    st.session_state.display = ""

def calculate():
    try:
        expr = st.session_state.display

        # Replace symbols with python operators
        expr = expr.replace("×", "*").replace("÷", "/")

        output = []
        num = ""

        for ch in expr:
            if ch.isdigit() or ch == ".":
                num += ch
            else:
                if num:
                    f, i = num.split(".")
                    inches = int(f) * 12 + int(i)
                    output.append(str(inches))
                    num = ""
                output.append(ch)

        if num:
            f, i = num.split(".")
            inches = int(f) * 12 + int(i)
            output.append(str(inches))

        inch_expr = "".join(output)
        result_inches = eval(inch_expr)

        result_feet = result_inches / 144
        st.session_state.display = str(round(result_feet, 4))

    except:
        st.session_state.display = "Error"

# -----------------------------
# Display (TOP)
# -----------------------------
st.text_input(
    "",
    value=st.session_state.display,
    disabled=True,
    key="display_box",
    label_visibility="collapsed"
)

# -----------------------------
# Calculator Layout
# -----------------------------
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["0", ".", "C", "+"],
]

for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        with cols[i]:
            if btn == "C":
                st.button(btn, use_container_width=True, on_click=clear)
            elif btn == "−":
                st.button(btn, use_container_width=True, on_click=press, args=("-",))
            else:
                st.button(btn, use_container_width=True, on_click=press, args=(btn,))

st.button("=", use_container_width=True, on_click=calculate)

# -----------------------------
# Footer
# -----------------------------
st.caption("Format: feet.inches → Example: 2.4 = (2×12)+4 inches → ÷144")
