import streamlit as st
from styles import load_styles

# Load styles
load_styles()

# ---- Email Settings Page ----
st.markdown('<div class="main-header"><h4 class="header-title">📧 Email Configuration</h4><p class="header-subtitle">Set up your gmail credentials to send emails directly</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Gmail Account Details</div>', unsafe_allow_html=True)

user_email = st.text_input("📧 Your Gmail Address:", placeholder="your-email@gmail.com")
app_password = st.text_input("🔑 App Password:", type="password", placeholder="sncc qwfd tbxo lxol")

with st.expander("ℹ️ How to get App Password"):
    st.markdown("""
    1. Go to your Google Account > Security
    2. Enable 2-Step Verification
    3. Go to 'App passwords'
    4. Select 'Mail' and your device
    5. Copy the generated password
    6. For more detailed steps: view https://youtu.be/MkLX85XU5rU?si=P0T1N-Bdd2Pc0m1p
    """)
    
if st.button("💾 Save Settings"):
    st.session_state.email_config = {"email": user_email, "password": app_password}
    st.success("✅ Email settings saved successfully!")

# Display current settings if they exist
if "email_config" in st.session_state and st.session_state.email_config.get("email"):
    st.markdown("### Current Settings")
    st.info(f"Email: {st.session_state.email_config.get('email')}")
    st.info("Password: *****" + (st.session_state.email_config.get("password")[-4:] if st.session_state.email_config.get("password") else ""))

# Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ by team <a href="https://github.com/suraj719/MailMate" target="_blank">status200</a>
    </div>
""", unsafe_allow_html=True)