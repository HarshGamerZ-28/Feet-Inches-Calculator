import streamlit as st

def convert_to_inches(value):
    try:
        feet, inches = value.split(".")
        return (int(feet) * 12) + int(inches)
    except Exception:
        return None

def custom_calc(expr):
    try:
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
            return "Invalid Expression!"

        inches1 = convert_to_inches(left.strip())
        inches2 = convert_to_inches(right.strip())
        if inches1 is None or inches2 is None:
            return "Invalid Input! Use feet.inches format"

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

if "expr" not in st.session_state:
    st.session_state.expr = ""

st.text_input("Expression", st.session_state.expr, key="expr_box")

buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", ".", "/", "C"]
]

for row in buttons:
    cols = st.columns(4)
    for i, b in enumerate(row):
        if cols[i].button(b):
            if b == "C":
                st.session_state.expr = ""
            else:
                st.session_state.expr += b

if st.button("Calculate"):
    result = custom_calc(st.session_state.expr)
    st.write("Result:", result)
