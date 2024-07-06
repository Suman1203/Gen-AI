import streamlit as st

# User credentials (for demonstration purposes)
USER_CREDENTIALS = {
    'Suman Biswas': 'Sumanbiswas@1234',
    'Sumit Biswas': 'Sumitbiswas@1234'
}

def login(username, password):
    """Check the username and password against the stored credentials."""
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        return True
    return False

def main():
    st.title("Login Page")

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.subheader("Please log in")
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if login(username, password):
                st.session_state.logged_in = True
                st.success("Logged in successfully")
            else:
                st.error("Invalid username or password")
    else:
        st.success("You are logged in")
        st.subheader("Welcome to the application!")
        # You can add more content for logged-in users here
        
        if st.button("Logout"):
            st.session_state.logged_in = False

if __name__ == '__main__':
    main()
