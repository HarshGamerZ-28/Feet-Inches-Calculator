import streamlit as st

# -----------------------------
# Page config (mobile friendly)
# -----------------------------
st.set_page_config(
    page_title="Feet Calculator",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    .stButton>button {
        height: 60px;
        font-size: 22px;
        border-radius: 12px;
    }
    .display-box input {
        font-size: 26px !important;
        text-align: right;
        height: 65px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📏 Feet–Inch Calculator")

# -----------------------------
# Session State
# -----------------------------
if "display" not in st.session_state:
    st.session_state.display = ""

# -----------------------------
# Functions
# -----------------------------
def press(val):
    st.session_state.display += val

def clear():
    st.session_state.display = ""

def calculate():
    try:
        expr = st.session_state.display.replace(" ", "")
        output = []
        number = ""

        for ch in expr:
            if ch.isdigit() or ch == ".":
                number += ch
            else:
                if number:
                    f, i = number.split(".")
                    total_inches = int(f) * 12 + int(i)
                    output.append(str(total_inches))
                    number = ""
                output.append(ch)

        if number:
            f, i = number.split(".")
            total_inches = int(f) * 12 + int(i)
            output.append(str(total_inches))

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
# Calculator Layout (Mobile)
# -----------------------------
layout = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
]

for row in layout:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        with cols[i]:
            if btn == "C":
                st.button(btn, use_container_width=True, on_click=clear)
            else:
                st.button(
                    btn,
                    use_container_width=True,
                    on_click=press,
                    args=(btn,)
                )

st.button("=", use_container_width=True, on_click=calculate)

# -----------------------------
# Helper text
# -----------------------------
st.caption("Example: 2.4 → (2×12)+4 inches → ÷144 feet")
