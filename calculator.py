# import streamlit as st

# # Function to perform the calculation
# def calculate(operation, num1, num2):
#     if operation == 'Add':
#         return num1 + num2
#     elif operation == 'Subtract':
#         return num1 - num2
#     elif operation == 'Multiply':
#         return num1 * num2
#     elif operation == 'Divide':
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return 'Error: Division by zero'

# # Streamlit application
# def main():
#     st.title("Simple Calculator")

#     num1 = st.number_input("Enter the first number", value=0.0)
#     num2 = st.number_input("Enter the second number", value=0.0)

#     operation = st.selectbox("Choose an operation", ['Add', 'Subtract', 'Multiply', 'Divide'])

#     if st.button("Calculate"):
#         result = calculate(operation, num1, num2)
#         st.write(f"The result of {operation.lower()}ing {num1} and {num2} is {result}")

# if __name__ == '__main__':
#     main()
import streamlit as st

# Function to perform the calculation
def calculate(operation, num1, num2):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by zero'

# Streamlit application


##############################################
# def main():
#     st.title("Number Plate Calculator")

#     # Define a list of numbers (number plate)
#     number_plate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#     st.write("Number Plate: ", number_plate)

#     # Select numbers from the number plate
#     num1 = st.selectbox("Choose the first number", number_plate)
#     num2 = st.selectbox("Choose the second number", number_plate)

#     operation = st.selectbox("Choose an operation", ['Add', 'Subtract', 'Multiply', 'Divide'])

#     if st.button("Calculate"):
#         result = calculate(operation, num1, num2)
#         st.write(f"The result of {operation.lower()}ing {num1} and {num2} is {result}")

# if __name__ == '__main__':
#     main()
######################################
import streamlit as st

# Function to perform the calculation
def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error: " + str(e)

# Streamlit application
def main():
    st.title("Interactive Calculator")

    # Initialize the expression in session state
    if 'expression' not in st.session_state:
        st.session_state.expression = ""

    st.write("Expression: " + st.session_state.expression)

    # Layout for the calculator buttons
    cols = st.columns(4)
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', 'C', '=', '+'
    ]

    for i, button in enumerate(buttons):
        if cols[i % 4].button(button):
            if button == 'C':
                st.session_state.expression = ""
            elif button == '=':
                st.session_state.expression = str(calculate(st.session_state.expression))
            else:
                st.session_state.expression += button

    # Display the result
    st.write("Result: " + st.session_state.expression)

if __name__ == '__main__':
    main()
