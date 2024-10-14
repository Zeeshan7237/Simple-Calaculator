import streamlit as st

# Global variables to store input and result
input_value = ""
operation = None
result = 0
calculated = False

# Function to perform calculation
def calculate():
    global input_value, result, operation, calculated
    try:
        if operation and input_value:
            if operation == "+":
                result += float(input_value)
            elif operation == "-":
                result -= float(input_value)
            elif operation == "*":
                result *= float(input_value)
            elif operation == "/":
                if float(input_value) != 0:
                    result /= float(input_value)
                else:
                    result = "Error"
            input_value = str(result)
            calculated = True
    except ValueError:
        result = "Error"

# Display for the calculator
st.markdown(f"<h1 style='text-align: right;'>{input_value or 0}</h1>", unsafe_allow_html=True)

# Layout structure
col1, col2 = st.columns([3, 1])

# Buttons for numbers and basic calculator operations
with col1:
    if st.button("CLEAR ENTRY", key="clear", help="Clears all inputs", use_container_width=True):
        input_value = ""
        result = 0
        operation = None

    st.write("")  # Empty space for alignment
    col_num1, col_num2, col_num3 = st.columns(3)
    
    if col_num1.button("7"):
        if calculated:
            input_value = ""
            calculated = False
        input_value += "7"
    if col_num2.button("8"):
        if calculated:
            input_value = ""
            calculated = False
        input_value += "8"
    if col_num3.button("9"):
        if calculated:
            input_value = ""
            calculated = False
        input_value += "9"

    col_num1, col_num2, col_num3 = st.columns(3)
    if col_num1.button("4"):
        if calculated:
            input_value = ""
            calculated = False
        input_value += "4"
    if col_num2.button("5"):
        if calculated:
            input_value = ""
            calculated = False
        input_value += "5"
    if col_num3.button("6"):
        if calculated:
            input_value = ""
            calculated = False
        input_value += "6"

    col_num1, col_num2, col_num3 = st.columns(3)
    if col_num1.button("1"):
        if calculated:
            input_value = ""
            calculated = False
        input_value += "1"
    if col_num2.button("2"):
        if calculated:
            input_value = ""
            calculated = False
        input_value += "2"
    if col_num3.button("3"):
        if calculated:
            input_value = ""
            calculated = False
        input_value += "3"

    col_num1, col_num2, col_num3 = st.columns(3)
    if col_num1.button("0"):
        if calculated:
            input_value = ""
            calculated = False
        input_value += "0"
    if col_num2.button("."):
        if calculated:
            input_value = ""
            calculated = False
        input_value += "."
    if col_num3.button("=", key="equals"):
        calculate()

# Operation buttons (+, -, *, /)
with col2:
    if st.button("+"):
        operation = "+"
        result = float(input_value) if input_value else 0
        input_value = ""
    if st.button("-"):
        operation = "-"
        result = float(input_value) if input_value else 0
        input_value = ""
    if st.button("x"):
        operation = "*"
        result = float(input_value) if input_value else 0
        input_value = ""
    if st.button("÷"):
        operation = "/"
        result = float(input_value) if input_value else 0
        input_value = ""

# Update the input display
st.markdown(f"<h1 style='text-align: right;'>{input_value or 0}</h1>", unsafe_allow_html=True)
