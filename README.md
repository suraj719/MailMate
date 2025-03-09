# 📩 MailMate AI - AI-Powered Email Generator

MailMate AI is a smart email assistant that helps you generate professional, engaging, and well-structured emails in seconds. Powered by Google's Gemini AI, MailMate AI crafts emails for various occasions, from formal business communication to friendly invitations.

## 🌟 Features
- ✨ **AI-Powered Email Generation** – Generate emails instantly for different tones and purposes.
- 🎨 **Beautiful HTML Formatting** – Option to create well-styled HTML emails.
- 📤 **Email Sending** – Send emails directly via your Gmail account.
- ⚙️ **Custom Email Settings** – Securely configure your Gmail credentials for seamless email dispatch.
- 🔒 **Secure & Private** – Uses Gmail App Passwords for secure authentication.

## 🚀 Live Demo
👉 **Try MailMate AI Now:** [Live Project Link](https://mailmate200.streamlit.app/) (Replace with actual link)

## 🛠️ Installation & Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/suraj719/MailMate.git
   cd MailMate
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   - Create a `.env` file in the project root directory.
   - Add your API key for Google Gemini AI:
   
   ```sh
   GENAI_API_KEY=your_google_gemini_api_key
   ```

5. **Run the Application:**
   ```sh
   streamlit run app.py
   ```

## 🛡️ Security & Privacy
- MailMate AI does **not store** your email credentials.
- Gmail App Passwords are used for authentication, ensuring security.
- AI-generated emails are not saved on any server.