import streamlit as st
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
if "templates" not in st.session_state:
    st.session_state.templates = load_templates()

# ---- Templates Page ----
st.markdown('<div class="main-header"><h4 class="header-title">📁 Email Templates</h4><p class="header-subtitle">Manage your email templates</p></div>', unsafe_allow_html=True)

# Refresh templates
st.session_state.templates = load_templates()

# Tabs for prebuilt and user templates
template_tab1, template_tab2 = st.tabs(["📚 Prebuilt Templates", "🔖 My Templates"])

with template_tab1:
    if not st.session_state.templates["prebuilt"]:
        st.info("No prebuilt templates available.")
    else:
        for name, template in st.session_state.templates["prebuilt"].items():
            with st.expander(f"📄 {name} ({template['type']})"):
                st.text_area("Template Content:", value=template["content"], height=200, key=f"prebuilt_{name}")
                
                if st.button("📝 Use Template", key=f"use_prebuilt_{name}"):
                    st.session_state.generated_email = template["content"]
                    st.session_state.template_type = template["type"]
                    st.session_state.template_html = template["html_format"]
                    st.success("✅ Template loaded! Go to the Email Generator page to use it.")

with template_tab2:
    if not st.session_state.templates["user"]:
        st.info("You haven't saved any templates yet. Generate an email and use the 'Save as Template' button to create one.")
    else:
        for name, template in st.session_state.templates["user"].items():
            with st.expander(f"📄 {name} ({template['type']})"):
                template_content = st.text_area("Template Content:", value=template["content"], height=200, key=f"user_{name}")
                
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    if st.button("📝 Use Template", key=f"use_{name}"):
                        st.session_state.generated_email = template["content"]
                        st.session_state.template_type = template["type"]
                        st.session_state.template_html = template["html_format"]
                        st.success("✅ Template loaded! Go to the Email Generator page to use it.")
                
                with col2:
                    if st.button("💾 Save Changes", key=f"save_{name}"):
                        save_template(name, template_content, template["type"], template["html_format"])
                        st.success("✅ Template updated successfully!")
                        st.rerun()
                
                with col3:
                    if st.button("🗑️ Delete", key=f"delete_{name}"):
                        templates = load_templates()
                        if name in templates["user"]:
                            del templates["user"][name]
                            with open(TEMPLATES_FILE, "w") as f:
                                json.dump(templates, f, indent=4)
                            st.success("✅ Template deleted successfully!")
                            st.rerun()

# Create new template manually section
st.markdown('<div class="section-title">Create New Template</div>', unsafe_allow_html=True)

new_template_name = st.text_input("Template Name:", placeholder="My Custom Template", key="new_template_name")
new_template_type = st.selectbox("Email Type:", ["Formal", "Cold e-mail", "Friendly", "Apologetic", "Sales Pitch", "Thank You"], key="new_template_type")
new_template_content = st.text_area("Template Content:", height=200, key="new_template_content", placeholder="Dear [Recipient Name],\n\nYour email content here...\n\nBest regards,\n[Your Name]")
new_template_html = st.checkbox("HTML Format", key="new_template_html")

if st.button("💾 Create Template") and new_template_name and new_template_content:
    save_template(new_template_name, new_template_content, new_template_type, new_template_html)
    st.success(f"✅ Template '{new_template_name}' created successfully!")
    st.rerun()

# Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ by team <a href="https://github.com/suraj719/MailMate" target="_blank">status200</a>
    </div>
""", unsafe_allow_html=True)