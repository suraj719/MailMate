import streamlit as st
from email_agent import EmailGenerator  # Import Email Generator class
import smtplib
from email.mime.text import MIMEText

# ---- 🎨 Streamlit UI Styling ----
st.set_page_config(page_title="MailMate - AI Email Generator", page_icon="📩", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #f7f9fc;
        }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            border-radius: 8px;
            padding: 12px;
            border: 1px solid #ddd;
        }
        .stButton>button {
            background: linear-gradient(90deg, #6a11cb, #2575fc);
            color: white;
            font-weight: 600;
            border-radius: 8px;
            padding: 12px 20px;
            border: none;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #2575fc, #6a11cb);
            transform: scale(1.05);
            color: white !important;
        }
        .email-box {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            font-family: 'Arial', sans-serif;
            line-height: 1.5;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 14px;
            color: #555;
        }
        .footer a {
            color: #2575fc;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- 🚀 Sidebar Navigation ----
st.sidebar.title("⚙️ Settings")
page = st.sidebar.radio("Navigate to:", ["📧 Email Settings", "📩 Email Generator"])

# ---- 📧 Email Settings Page ----
if page == "📧 Email Settings":
    st.title("📧 Email Configuration")
    st.write("Enter your **Gmail & App Password** to enable email sending.")

    # Store credentials using session state
    if "email_config" not in st.session_state:
        st.session_state.email_config = {"email": "", "password": ""}

    user_email = st.text_input("📧 Your Gmail Address:", value=st.session_state.email_config["email"], placeholder="e.g., your-email@gmail.com")
    app_password = st.text_input("🔑 App Password:", value=st.session_state.email_config["password"], type="password", placeholder="Generated App Password")

    if st.button("💾 Save Email Settings"):
        st.session_state.email_config = {"email": user_email, "password": app_password}
        st.success("✅ Email settings saved successfully!")

# ---- 📩 Email Generator Page ----
elif page == "📩 Email Generator":
    st.title("📩 MailMate - AI Email Generator")
    st.write("### AI-powered emails that sound like *you* – professional, personal yet simple!!! 🚀")

    st.subheader("💌 Craft Your Email")
    recipient_name = st.text_input("👤 Recipient Name:")
    recipient_email = st.text_input("📧 Recipient Email:", placeholder="e.g., recipient@example.com")
    event_name = st.text_input("🎉 Event Name:")
    special_instructions = st.text_area("📝 Special Instructions (optional):", placeholder="e.g., Keep it formal, add humor, mention a discount...")

    # Generate Email Button
    if st.button("✨ Generate Email"):
        if recipient_name and event_name:
            agent = EmailGenerator("MailMate AI")
            email_body = agent.generate_email(recipient_name, event_name, special_instructions)

            # Store email content in session state for preview
            st.session_state.generated_email = email_body

    # Display Email Preview if generated
    if "generated_email" in st.session_state:
        st.markdown("### 📄 Your AI-Generated Email:")
        email_content = st.text_area("📝 Edit Before Sending:", value=st.session_state.generated_email, height=200)
        
        # Update session state with edited content
        st.session_state.generated_email = email_content

        # Send Email Button
        if st.button("📤 Send Email"):
            if recipient_email:
                # sender_email = st.session_state.email_config.get("email")
                # sender_password = st.session_state.email_config.get("password")
                sender_email = "gitty695@gmail.com"
                sender_password = "sncc qwfd tbxo lxop"

                if sender_email and sender_password:
                    try:
                        smtp_server = "smtp.gmail.com"
                        smtp_port = 465  # SSL Port

                        msg = MIMEText(st.session_state.generated_email, "plain")
                        msg["From"] = sender_email
                        msg["To"] = recipient_email
                        msg["Subject"] = f"Regarding {event_name}"

                        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                            server.login(sender_email, sender_password)
                            server.sendmail(sender_email, recipient_email, msg.as_string())

                        st.success("✅ Email sent successfully!")

                    except Exception as e:
                        st.error(f"❌ Failed to send email: {str(e)}")
                else:
                    st.error("⚠️ Please save your email settings in '📧 Email Settings'.")
            else:
                st.error("⚠️ Please enter the recipient's email.")

# ---- 🎉 Footer ----
st.markdown(
    """
    <div class="footer">
        Made with ❤️ by <a href="https://github.com/suraj719/MailMate" target="_blank">team status200</a>
    </div>
    """,
    unsafe_allow_html=True,
)
