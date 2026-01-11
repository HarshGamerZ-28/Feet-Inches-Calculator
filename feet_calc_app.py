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
# CSS (force mobile grid + dark display)
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

def calculate():
    try:
        expr = st.session_state.display.replace("×", "*").replace("÷", "/")

        output = []
        num = ""

        for ch in expr:
            if ch.isdigit() or ch == ".":
                num += ch
            else:
                if num:
                    if "." in num:
                        f, i = num.split(".")
                        inches = int(f) * 12 + int(i)
                    else:
                        inches = int(num) * 12
                    output.append(str(inches))
                    num = ""
                output.append(ch)

        if num:
            if "." in num:
                f, i = num.split(".")
                inches = int(f) * 12 + int(i)
            else:
                inches = int(num) * 12
            output.append(str(inches))

        inch_expr = "".join(output)
        result_inches = eval(inch_expr)

        # ✅ FINAL CORRECT STEP
        result_feet = result_inches / 12

        st.session_state.display = str(round(result_feet, 2))

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
# Calculator Buttons (mobile fixed)
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

st.caption("2.4 → (2×12)+4 | Final result ÷ 12")
