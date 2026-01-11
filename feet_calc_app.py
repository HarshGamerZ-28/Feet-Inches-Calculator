import streamlit as st

# --- Conversion helper ---
def convert_to_inches(value):
    try:
        if "." in value:
            feet, inches = value.split(".")
            return (int(feet) * 12) + int(inches)
        else:
            return int(value) * 12
    except Exception:
        return None

# --- Calculator logic ---
def custom_calc(expr):
    try:
        if "+" in expr:
            left, right = expr.split("+")
            op = "+"
        elif "*" in expr:
            left, right = expr.split("*")
            op = "*"
        else:
            return "Only + and * supported!"

        inches1 = convert_to_inches(left.strip())
        inches2 = convert_to_inches(right.strip())
        if inches1 is None or inches2 is None:
            return "Invalid Input! Use feet.inches format"

        if op == "+":
            result = inches1 + inches2
        elif op == "*":
            result = (inches1 * inches2) / 144  # square feet

        return round(result, 1)
    except Exception:
        return "Error in calculation!"

# --- Streamlit UI ---
st.title("Feet.Inches Calculator 🧮")

# Internal state (not bound to widget)
if "expr" not in st.session_state:
    st.session_state["expr"] = ""

# Show current expression in a text box (read-only)
st.text_input("Expression", value=st.session_state["expr"], key="expr_box")

# Calculate button
if st.button("Calculate"):
    result = custom_calc(st.session_state["expr"])
    st.subheader("Result:")
    st.write(result)

# Keypad layout
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "C"],
    ["0", ".", "/", "="]  # "/" included but not supported in calc
]

for row in buttons:
    cols = st.columns(len(row))
    for i, b in enumerate(row):
        if cols[i].button(b, use_container_width=True):
            if b == "C":
                st.session_state["expr"] = ""
            elif b == "=":
                result = custom_calc(st.session_state["expr"])
                st.subheader("Result:")
                st.write(result)
            else:
                st.session_state["expr"] = st.session_state["expr"] + b
            # update display
            st.session_state["expr_box"] = st.session_state["expr"]
