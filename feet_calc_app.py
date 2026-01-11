import streamlit as st

# Conversion function: feet.inches → inches
def convert_to_inches(value):
    try:
        feet, inches = value.split(".")
        return (int(feet) * 12) + int(inches)
    except Exception:
        return None

# Calculator logic
def custom_calc(expr):
    try:
        # Split by operator
        if "+" in expr:
            left, right = expr.split("+")
            op = "+"
        elif "-" in expr:
            left, right = expr.split("-")
            op = "-"
        elif "*" in expr:
            left, right = expr.split("*")
            op = "*"
        elif "/" in expr:
            left, right = expr.split("/")
            op = "/"
        else:
            return "Invalid Expression! Use format like 2.4*10.1"

        inches1 = convert_to_inches(left.strip())
        inches2 = convert_to_inches(right.strip())
        if inches1 is None or inches2 is None:
            return "Invalid Input! Use feet.inches format (e.g., 2.6*3.4)"

        if op == "+":
            result = inches1 + inches2
        elif op == "-":
            result = inches1 - inches2
        elif op == "*":
            result = (inches1 * inches2) / 144
        elif op == "/":
            if inches2 == 0:
                return "Division by zero!"
            result = inches1 / inches2

        return round(result, 1)
    except Exception:
        return "Error in calculation!"

# --- Streamlit UI ---
st.title("Feet.Inches Calculator 🧮")

# Calculator-style buttons
if "expr" not in st.session_state:
    st.session_state.expr = ""

st.text_input("Expression", st.session_state.expr, key="expr_box")

cols = st.columns(4)
buttons = ["7","8","9","+","4","5","6","-","1","2","3","*","0",".","/","C"]

for i, b in enumerate(buttons):
    if cols[i % 4].button(b):
        if b == "C":
            st.session_state.expr = ""
        else:
            st.session_state.expr += b
        st.experimental_rerun()

if st.button("Calculate"):
    result = custom_calc(st.session_state.expr)
    st.write("Result:", result)
