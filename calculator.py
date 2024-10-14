import streamlit as st

# Global variables to store the current input, result, and operator
current_input = ""
result = 0
operator = None

# Function to perform calculation based on the operator
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error"

# Streamlit layout
st.title("Simple Calculator")

# Input display
input_display = st.text_input("Display", value=str(current_input), key="input_display", disabled=True)

# Divide the layout into columns
col1, col2, col3 = st.columns([2, 1, 1])

# Number buttons
with col1:
    st.write("")
    if st.button("0"):
        current_input += "0"
    if st.button("1"):
        current_input += "1"
    if st.button("2"):
        current_input += "2"
    if st.button("3"):
        current_input += "3"
    if st.button("4"):
        current_input += "4"
    if st.button("5"):
        current_input += "5"
    if st.button("6"):
        current_input += "6"
    if st.button("7"):
        current_input += "7"
    if st.button("8"):
        current_input += "8"
    if st.button("9"):
        current_input += "9"
    if st.button("."):
        current_input += "."

# Operation buttons and equal
with col2:
    st.write("")
    if st.button("+"):
        operator = "+"
        result = float(current_input)
        current_input = ""
    if st.button("-"):
        operator = "-"
        result = float(current_input)
        current_input = ""
    if st.button("x"):
        operator = "*"
        result = float(current_input)
        current_input = ""
    if st.button("÷"):
        operator = "/"
        result = float(current_input)
        current_input = ""

# Clear and equal button
with col3:
    st.write("")
    if st.button("CLEAR ENTRY"):
        current_input = ""
        result = 0
        operator = None

    if st.button("="):
        result = calculate(result, float(current_input), operator)
        current_input = str(result)

# Update the display
st.text_input("Display", value=str(current_input), key="output_display", disabled=True)
