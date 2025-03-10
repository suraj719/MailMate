import streamlit as st
from email_generator import EmailGenerator
from email_sender import EmailSender
import json
import os
from styles import load_styles

# Load styles
load_styles()

# ---- Templates functionality ----
TEMPLATES_FILE = "email_templates.json"

# Default prebuilt templates
DEFAULT_TEMPLATES = {
    "Meeting Request": {
        "content": """Dear [Recipient Name],

I hope this email finds you well. I would like to request a meeting to discuss [Brief Topic Description]. Your insights would be valuable for our upcoming decisions.

Could we schedule a [Duration] meeting on [Proposed Date/Time]? If this doesn't work for you, please suggest a more convenient time.

Thank you for considering my request. I look forward to our conversation.

Best regards,
[Your Name]""",
        "type": "Formal",
        "html_format": False
    },
    "Job Application Follow-up": {
        "content": """Dear [Recipient Name],

I hope this email finds you well. I am writing to follow up on my application for the [Position] role that I submitted on [Date].

I remain very interested in the opportunity to join [Company Name] and contribute to your team. I'm particularly excited about [specific aspect of the company/role].

Please let me know if you need any additional information from my end to support my application.

Thank you for your time and consideration.

Best regards,
[Your Name]""",
        "type": "Formal",
        "html_format": False
    },
    "Thank You - Event": {
        "content": """Dear [Recipient Name],

Thank you so much for organizing [Event Name]. It was a wonderful experience, and I particularly enjoyed [specific aspect of the event].

The insights shared during the event will be valuable for my [personal/professional] development. I appreciate the effort you put into making this event successful.

Looking forward to attending more such events in the future.

Warm regards,
[Your Name]""",
        "type": "Thank You",
        "html_format": False
    }
}

def load_templates():
    if os.path.exists(TEMPLATES_FILE):
        try:
            with open(TEMPLATES_FILE, "r") as f:
                templates = json.load(f)
                # Ensure both sections exist
                if "prebuilt" not in templates:
                    templates["prebuilt"] = DEFAULT_TEMPLATES
                if "user" not in templates:
                    templates["user"] = {}
                return templates
        except:
            return {"prebuilt": DEFAULT_TEMPLATES, "user": {}}
    else:
        # File doesn't exist, create default structure
        default_structure = {"prebuilt": DEFAULT_TEMPLATES, "user": {}}
        # Save the default structure
        with open(TEMPLATES_FILE, "w") as f:
            json.dump(default_structure, f, indent=4)
        return default_structure

def save_template(name, content, email_type, html_format):
    templates = load_templates()
    templates["user"][name] = {
        "content": content,
        "type": email_type,
        "html_format": html_format
    }
    with open(TEMPLATES_FILE, "w") as f:
        json.dump(templates, f, indent=4)

# ---- Session state initialization ----
if "generated_email" not in st.session_state:
    st.session_state.generated_email = ""
    
# Initialize templates
if "templates" not in st.session_state:
    st.session_state.templates = load_templates()

# ---- Email Generator Page ----
st.markdown('<div class="main-header"><h1 class="header-title">📩 MailMate</h1><p class="header-subtitle">Your AI-powered email assistant that crafts professional, personalized emails effortlessly!!🚀</p></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">📝 Compose Your Email</div>', unsafe_allow_html=True)

# Template selection feature
all_templates = {}

# Ensure templates are properly loaded
if "templates" in st.session_state and st.session_state.templates:
    if "prebuilt" in st.session_state.templates:
        all_templates.update(st.session_state.templates["prebuilt"])
    if "user" in st.session_state.templates:
        all_templates.update(st.session_state.templates["user"])

template_options = ["No template"] + list(all_templates.keys())

selected_template = st.selectbox("📋 Start with a template:", template_options)

# If a template is selected, pre-fill the fields
if selected_template != "No template" and selected_template in all_templates:
    template_data = all_templates[selected_template]
    st.session_state.generated_email = template_data["content"]
    template_type = template_data["type"]
    use_html_format = template_data["html_format"]
else:
    template_type = ""
    use_html_format = False

# Input Fields
recipient_name = st.text_input("👤 Recipient Name:", placeholder="suraj thammi")
recipient_email = st.text_input("📧 Recipient Email:", placeholder="e.g., recipient@example.com")
event_name = st.text_input("🎉 Subject/short intro:", placeholder="Invitation to technical webinar... etc")

# Email type options
email_type_options = ["Formal", "Cold e-mail", "Friendly", "Apologetic", "Sales Pitch", "Thank You"]

# Use template type if available, otherwise allow selection
if template_type and selected_template != "No template" and template_type in email_type_options:
    email_type = st.selectbox("✉️ Email Type:", email_type_options, index=email_type_options.index(template_type))
else:
    email_type = st.selectbox("✉️ Email Type:", email_type_options)

special_instructions = st.text_area("📝 Additional details (optional):", placeholder="Details of reciever, details related to event, Job Description etc....")

# Use template HTML format if available, otherwise allow selection
if selected_template != "No template":
    use_html_format = st.checkbox("📜 Create Beautiful Email with HTML (recommended for better visuals and formatting)", value=use_html_format)
else:
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
    
    # Save as template option
    # col1, col2 = st.columns([1, 1])
    # with col1:
    template_name = st.text_input("Template Name:", placeholder="My Professional Introduction")
    # with col2:
    if st.button("💾 Save as Template") and template_name:
        save_template(template_name, st.session_state.generated_email, email_type, use_html_format)
        st.success(f"✅ Template '{template_name}' saved successfully!")
            # Refresh templates in session state
        st.session_state.templates = load_templates()
            
    if recipient_email:
        if st.button("📤 Send Email Now"):
            email_body = st.session_state.generated_email
            sender = EmailSender()
            result = sender.sendEmail(recipient_email, event_name, email_body, use_html_format)
            if(result.get("success")):
                st.success(result.get("msg"))
            else:
                st.error(result.get("msg"))

# Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ by team <a href="https://github.com/suraj719/MailMate" target="_blank">status200</a>
    </div>
""", unsafe_allow_html=True)