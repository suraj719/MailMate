import smtplib
import streamlit as st
from email.mime.text import MIMEText

class EmailSender:
    def sendEmail(self, recipient_email, event_name, email_content, use_html_format=False):
        sender_email = st.session_state.email_config.get("email")
        sender_password = st.session_state.email_config.get("password")

        if sender_email and sender_password:
            try:
                smtp_server = "smtp.gmail.com"
                smtp_port = 465

                msg = MIMEText(email_content, "html" if use_html_format else "plain")
                msg["From"] = sender_email
                msg["To"] = recipient_email
                msg["Subject"] = f"Regarding {event_name}"

                with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, recipient_email, msg.as_string())

                return {
                    "success": True,
                    "msg": "✅ Email sent successfully!"
                }

            except Exception as e:
                return {
                    "success": False,
                    "msg": f"❌ Failed to send email: {str(e)}"
                }
        else:
            return {
                "success": False,
                "msg": "⚠️ Please configure your email settings in the 'Email Settings' tab first."
            }