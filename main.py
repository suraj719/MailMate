import streamlit as st
from styles import load_styles

# ---- Load styles ----
st.set_page_config(page_title="MailMate - Personalized Email Generator", page_icon="📩", layout="centered")
load_styles()

# Main home page
st.markdown('<div class="main-header"><h1 class="header-title">📩 MailMate</h1><p class="header-subtitle">Your AI-powered email assistant that crafts professional, personalized emails effortlessly!🚀</p></div>', unsafe_allow_html=True)

# Welcome section with improved styling
st.markdown("""
<div class="welcome-section">
    <h2>Welcome to MailMate!</h2>
    <p>MailMate helps you create professional, personalized emails with just a few clicks. Navigate through the pages on the sidebar to:</p>
    <ul>
        <li><strong>📩 Generate Emails</strong>: Create customized emails for any situation</li>
        <li><strong>📧 Configure Email Settings</strong>: Set up your Gmail credentials for sending emails</li>
        <li><strong>📁 Manage Templates</strong>: Browse, create, and manage email templates</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Call to action button
st.markdown("""
<div style="text-align: center;">
    <a href="Email_Generator" class="cta-button">Generate an Email Now</a>
</div>
""", unsafe_allow_html=True)

# Features showcase with improved cards
st.markdown("<h3>✨ Key Features</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">AI-Powered</div>
        <div class="feature-description">Leverage AI to craft perfectly worded emails for any context or situation</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📋</div>
        <div class="feature-title">Templates</div>
        <div class="feature-description">Choose from pre-built templates or save your own for future use</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📤</div>
        <div class="feature-title">Direct Sending</div>
        <div class="feature-description">Send emails directly through your Gmail account with ease</div>
    </div>
    """, unsafe_allow_html=True)

# How it works section
st.markdown("<h3>🔍 How It Works</h3>", unsafe_allow_html=True)
st.markdown("""
<div class="steps-container">
    <div class="step">
        <div class="step-number">1</div>
        <div class="step-content">
            <div class="step-title">Select a Template</div>
            <div class="step-description">Choose from our pre-built templates or start from scratch</div>
        </div>
    </div>
    <div class="step">
        <div class="step-number">2</div>
        <div class="step-content">
            <div class="step-title">Customize Your Email</div>
            <div class="step-description">Fill in the details or let AI generate content based on your needs</div>
        </div>
    </div>
    <div class="step">
        <div class="step-number">3</div>
        <div class="step-content">
            <div class="step-title">Send</div>
            <div class="step-description">Send the customized email directly via Gmail SMTP server</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)



# Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ by team <a href="https://github.com/suraj719/MailMate" target="_blank">status200</a>
    </div>
""", unsafe_allow_html=True)