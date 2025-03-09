import streamlit as st
from email_agent import EmailGenerator  # Import our email generator agent

# Initialize the Email Generator Agent
agent = EmailGenerator("AI Email Assistant")

# Streamlit UI
st.title("📧 AI Personalized Email Generator")
st.write("Generate personalized emails effortlessly with AI.")

# Sidebar for settings
st.sidebar.header("Settings")

# Email Form
st.subheader("✉️ Compose Your Email")
recipient_name = st.text_input("Recipient Name:")
event_name = st.text_input("Event Name:")
special_instructions = st.text_area("Special Instructions:")

if st.button("Generate Email"):
    if recipient_name and event_name:
        email_body = agent.generate_email(recipient_name, event_name, special_instructions)
        st.write("### Generated Email:")
        st.write(email_body)
    else:
        st.error("Please provide both Recipient Name and Event Name.")

# Run with: streamlit run app.py