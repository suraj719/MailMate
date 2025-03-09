import streamlit as st

def load_styles():
    st.markdown("""
    <style>
    /* Base styling with better spacing */
.block-container {
  padding-top: 2rem;
  padding-bottom: 2rem;
  max-width: 1000px;
}

/* Section styling (replacing cards) */
.section {
  background-color: #f8f9fa;
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 24px;
  border: 1px solid #e9ecef;
}

.section-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 20px;
  color: white;
  border-bottom: 1px solid #e9ecef;
  padding-bottom: 10px;
}
/* Remove resize handle from text area */
.stTextArea > div > div > textarea {
  resize: none !important;
}

/* Remove any default browser autofill UI */
.stTextInput > div > div > input::-webkit-autofill,
.stTextInput > div > div > input::-webkit-autofill:hover,
.stTextInput > div > div > input::-webkit-autofill:focus,
.stTextInput > div > div > input::-webkit-autofill:active {
  background-color: transparent !important;
  color: inherit !important;
  box-shadow: none !important;
  border: none !important;
  -webkit-text-fill-color: inherit !important;
  transition: background-color 5000s ease-in-out 0s !important;
}

/* Remove any extra UI elements like password reveal, autofill icons, etc. */
.stTextInput > div > div > input::-ms-reveal,
.stTextInput > div > div > input::-ms-clear,
.stTextInput > div > div > input::-webkit-contacts-auto-fill-button,
.stTextInput > div > div > input::-webkit-credentials-auto-fill-button {
  display: none !important;
  visibility: hidden !important;
  pointer-events: none !important;
}

/* Completely hide any hidden pseudo-elements causing the bubble */
.stTextInput > div:after,
.stTextInput > div > div:after {
  content: none !important;
  display: none !important;
}

/* Ensure uniform styling for all elements */

.stSelectbox > div > div,
.stMultiSelect > div > div {
  border-radius: 10px;
  border: 1px solid white !important;
  box-shadow: none !important;
  outline: none !important;
  transition: border-color 0.3s ease;
  background-color: transparent !important;
}

/* Remove any default Streamlit box shadow */
.stTextInput > div > div,
.stTextArea > div > div {
  border: none !important;
  background-color: transparent !important;
  box-shadow: none !important;
}

/* Target ALL states including hover, focus, active */
.stTextInput > div:hover,
.stTextArea > div:hover,
.stTextInput > div:focus-within,
.stTextArea > div:focus-within,
.stSelectbox > div > div:hover,
.stMultiSelect > div > div:hover,
.stSelectbox > div > div:focus-within,
.stMultiSelect > div > div:focus-within {
  border: 1px solid #4a90e2 !important;
  box-shadow: none !important;
  outline: none !important;
}

/* Override Streamlit's default styling */
.stTextInput div[data-baseweb="input"],
.stTextArea div[data-baseweb="textarea"],
.stSelectbox div[data-baseweb="select"],
.stMultiSelect div[data-baseweb="select"] {
  border-color: white !important;
  box-shadow: none !important;
}

.stTextInput div[data-baseweb="input"]:focus-within,
.stTextArea div[data-baseweb="textarea"]:focus-within,
.stSelectbox div[data-baseweb="select"]:focus-within,
.stMultiSelect div[data-baseweb="select"]:focus-within {
  border-color: #4a90e2 !important;
  box-shadow: none !important;
}

/* Button styling with adjusted margins */
.stButton > button {
  background: linear-gradient(90deg, #2575fc, #6a11cb);
  color: white;
  font-weight: 600;
  border-radius: 8px;
  padding: 12px 20px;
  border: none;
  transition: all 0.3s ease-in-out;
  margin: 10px 0;
  width: 100%;
}
.stButton > button:hover {
  background: linear-gradient(90deg, #6a11cb, #2575fc);
  color: white !important;
  transform: scale(1.02);
}

/* Email preview with adjusted padding */
.email-preview {
  background: #ffffff;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
  font-family: "Arial", sans-serif;
  line-height: 1.5;
  border: 1px solid #ddd;
  color: #333;
  max-height: 500px;
  overflow-y: auto;
  margin: 15px 0;
}

/* Tabs styling with improved spacing */
.tab-content {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 0 0 8px 8px;
  margin: 0;
}

/* Footer */
.footer {
  text-align: center;
  margin-top: 30px;
  font-size: 14px;
  color: #807e7e;
  padding: 15px 0 25px 0;
}
.footer a {
  color: #2575fc;
  text-decoration: none;
  font-weight: bold;
}
.footer a:hover {
  text-decoration: underline;
}

/* Tabs specific styling */
.stTabs [data-baseweb="tab-list"] {
  gap: 0px;
}
.stTabs [data-baseweb="tab"] {
  height: 50px;
  white-space: pre-wrap;
  background-color: #f0f2f6;
  border-radius: 8px 8px 0 0;
  border: 1px solid #ddd;
  border-bottom: none;
  padding: 15px;
}
.stTabs [aria-selected="true"] {
  background-color: white;
  border-bottom: 1px solid white;
}

/* Header styling */
.main-header {
  background: linear-gradient(90deg, #6a11cb, #2575fc);
  padding: 10px 10px;
  border-radius: 12px;
  color: white;
  margin-bottom: 30px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}
.header-title {
  font-size: 28px !important;
  font-weight: bold;
  margin: 0;
}
.header-subtitle {
  font-size: 16px;
  opacity: 0.9;
  margin-top: 8px;
}

/* Labels with better spacing */
label {
  font-weight: 500;
  margin-bottom: 8px;
  display: block;
}

/* Fix for white space */
div[data-testid="stVerticalBlock"] {
  gap: 15px !important;
}

/* Sidebar improvements */
.css-6qob1r {
  padding: 2rem 1rem;
}

/* Expander styling */
.streamlit-expanderHeader {
  font-weight: 500;
  color: #2575fc;
}

/* Selectbox styling */
.stSelectbox {
  margin-bottom: 10px;
}
div[role="tablist"] button {
  font-size: 18px !important;
  font-weight: bold !important;
  background-color: #f0f0f0 !important;
  color: #333 !important;
  padding: 10px !important;
  margin-right: 5px !important;
}
    </style>
    """, unsafe_allow_html=True)
