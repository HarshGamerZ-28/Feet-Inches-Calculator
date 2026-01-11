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
# CSS (Dark display + big buttons)
# -----------------------------
st.markdown("""
<style>
.calc-display {
    width: 100%;
    background: #000000;
    color: #ffffff;
    padding: 18px;
    font-size: 30px;
    text-align: right;
    border-radius: 14px;
    margin-bottom: 15px;
    min-height: 70px;
    box-sizing: border-box;
}
.stButton>button {
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

def clear():
    st.session_state.display = ""

def delete():
    st.session_state.display = st.session_state.display[:-1]

def calculate():
    try:
        expr = st.session_state.display
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

        # Final conversion to feet
        result_feet = result_inches / 144
        st.session_state.display = str(round(result_feet, 4))

    except:
        st.session_state.display = "Error"

# -----------------------------
# Display (TOP)
# -----------------------------
st.markdown(
    f"<div class='calc-display'>{st.session_state.display}</div>",
    unsafe_allow_html=True
)

# -----------------------------
# Calculator Buttons
# -----------------------------
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["0", ".", "⌫", "+"],
]

for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        with cols[i]:
            if btn == "⌫":
                st.button(btn, use_container_width=True, on_click=delete)
            elif btn == "−":
                st.button(btn, use_container_width=True, on_click=press, args=("-",))
            else:
                st.button(btn, use_container_width=True, on_click=press, args=(btn,))

st.button("C", use_container_width=True, on_click=clear)
st.button("=", use_container_width=True, on_click=calculate)

# -----------------------------
# Footer
# -----------------------------
st.caption("Example: 2.4 → (2×12)+4 inches → ÷144 feet")
