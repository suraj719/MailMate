import google.generativeai as genai
import re

class EmailGenerator:
    def __init__(self, name="MailMate AI"):
        self.name = name

    def generate_email(self, recipient_name, event_name, email_type, special_instructions="", use_html=False):
        """Generates a structured, professional email using AI."""
        prompt = f"""
        You are an expert email composer. Create a {email_type.lower()} email for {recipient_name} regarding {event_name}.
        
        IMPORTANT: Return ONLY the exact email content. NO explanations, NO markdown formatting, and NO extra text.

        The email must include:
        - A proper greeting
        - A structured body
        - A professional closing with a signature

        Additional information: {special_instructions}
        - Format: {"HTML" if use_html else "Plain text"}
        """

        response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)
        email_content = response.text.strip() if response else "Error generating email content."

        # Cleanup text
        email_content = re.sub(r'^(Here\'s|Here is|I\'ve created|Below is|This is|As requested|Please find)(.*?)email[:\s]*', '', email_content, flags=re.IGNORECASE|re.DOTALL)
        email_content = re.sub(r'```html\s*', '', email_content)
        email_content = re.sub(r'```\s*', '', email_content)

        # If HTML is requested but response lacks HTML structure, wrap it
        if use_html and not email_content.lower().startswith('<html'):
            email_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Email</title>
            </head>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333333; max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9;">
                <div style="background-color: #ffffff; padding: 30px; border-radius: 10px; box-shadow: 0 3px 10px rgba(0,0,0,0.1);">
                    {email_content}
                </div>
            </body>
            </html>
            """
        return email_content
