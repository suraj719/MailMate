import streamlit as st
from email_generator import EmailGenerator
from email_sender import EmailSender
from styles import load_styles
import config

# ---- Load styles ----
st.set_page_config(page_title="MailMate - personalized Email Generator", page_icon="📩", layout="centered")
load_styles()

# ---- Sidebar Navigation ----
with st.sidebar:
    st.title("⚙️ Settings")
    page = st.radio("Navigate to:", ["📩 Email Generator","📧 Email Settings"])

# ---- Session state initialization ----
if "generated_email" not in st.session_state:
    st.session_state.generated_email = ""

# ---- 📧 Email Settings Page ----
if page == "📧 Email Settings":
    st.markdown('<div class="main-header"><h4 class="header-title">📧 Email Configuration</h4><p class="header-subtitle">Set up your gmail credentials to send emails directly</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Gmail Account Details</div>', unsafe_allow_html=True)

    user_email = st.text_input("📧 Your Gmail Address:",placeholder="your-email@gmail.com")
    app_password = st.text_input("🔑 App Password:", type="password",placeholder="sncc qwfd tbxo lxol")
    
    with st.expander("ℹ️ How to get App Password"):
        st.markdown("""
        1. Go to your Google Account > Security
        2. Enable 2-Step Verification
        3. Go to 'App passwords'
        4. Select 'Mail' and your device
        5. Copy the generated password
        for more detailed steps: view https://youtu.be/MkLX85XU5rU?si=P0T1N-Bdd2Pc0m1p
        """)
        
    if st.button("💾 Save Settings"):
        st.session_state.email_config = {"email": user_email, "password": app_password}
        st.session_state.page = "📩 Email Generator"
        st.success("✅ Email settings saved successfully!")

# ---- 📩 Email Generator Page ----
elif page == "📩 Email Generator":
    st.markdown('<div class="main-header"><h1 class="header-title">📩 MailMate</h1><p class="header-subtitle">Your AI-powered email assistant that crafts professional, personalized emails effortlessly!!🚀</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Compose Your Email</div>', unsafe_allow_html=True)

    # Input Fields
    recipient_name = st.text_input("👤 Recipient Name:", placeholder="suraj thammi")
    recipient_email = st.text_input("📧 Recipient Email:", placeholder="e.g., recipient@example.com")
    event_name = st.text_input("🎉 Subject/short intro:", placeholder="Invitation to technical webinar... etc")
    email_type = st.selectbox("✉️ Email Type:", ["Formal","Cold e-mail", "Friendly", "Apologetic", "Sales Pitch", "Thank You"])
    special_instructions = st.text_area("📝 Additional details (optional):",placeholder="Details of reciever, details related to event, Job Description etc....")
    use_html_format = st.checkbox("📜 Create Beautiful Email with HTML (recommended for better visuals and formatting)")

    if st.button("✨ Generate Email"):
        if event_name:
            with st.spinner("Crafting your email 🪄..."):
                agent = EmailGenerator()
                email_body = agent.generate_email(recipient_name, event_name, email_type, special_instructions, use_html_format)
                st.session_state.generated_email = email_body
                st.success("✅ Email generated successfully!")
        else:
            st.error("⚠️ Please fill in 'Subject/short intro' field to generate an email.")

    # Display Generated Email
    if st.session_state.generated_email:
        st.markdown('<div class="section-title">📄 Your AI-Generated Email</div>', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["📋 Preview", "✏️ Edit"])
        
        with tab1:
            if use_html_format:
                # Display the HTML content properly rendered
                st.components.v1.html(st.session_state.generated_email, height=400, scrolling=True)
            else:
                # For plain text, use a styled div but avoid showing HTML tags
                formatted_email = st.session_state.generated_email.replace('\n', '<br>')
                st.markdown(f"<div class='email-preview'>{formatted_email}</div>", unsafe_allow_html=True)
        
        with tab2:
            # Edit mode
            email_content = st.text_area("Edit Your Email:", value=st.session_state.generated_email, height=300)
            if st.button("💾 Save Changes"):
                st.session_state.generated_email = email_content
                st.success("✅ Changes saved!")
                
        if recipient_email:
            if st.button("📤 Send Email Now"):
                email_body = st.session_state.generated_email
                sender = EmailSender()
                result = sender.sendEmail(recipient_email, event_name, email_body, use_html_format)
                # st.success(result)
                if(result.get("success")):
                    st.success(result.get("msg"))
                else:
                    st.error(result.get("msg"))

# ---- 🎉 Footer ----
st.markdown("""
    <div class="footer">
        Made with ❤️ by team <a href="https://github.com/suraj719/MailMate" target="_blank">status200</a>
    </div>
""", unsafe_allow_html=True)