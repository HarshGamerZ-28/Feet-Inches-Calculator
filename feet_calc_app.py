# --- Streamlit UI ---
st.title("Feet.Inches Calculator 🧮")

if "expr" not in st.session_state:
    st.session_state.expr = ""

st.text_input("Expression", st.session_state.expr, key="expr_box")

# Calculator buttons arranged in rows
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
