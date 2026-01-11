import streamlit as st

def convert_to_inches(value):
    try:
        feet, inches = value.split(".")
        return (int(feet) * 12) + int(inches)
    except Exception:
        return None

def custom_calc(expression):
    try:
        left, right = expression.split("*")
        inches1 = convert_to_inches(left.strip())
        inches2 = convert_to_inches(right.strip())
        if inches1 is None or inches2 is None:
            return "Invalid Input! Use feet.inches format (e.g., 2.6*3.4)"
        result = (inches1 * inches2) / 144
        return round(result, 1)
    except Exception:
        return "Invalid Expression! Use format like 2.4*10.1"

st.title("Feet.Inches Calculator 📱")
expr = st.text_input("Enter expression (e.g., 2.4*10.1)")
if st.button("Calculate"):
    st.write("Result:", custom_calc(expr))