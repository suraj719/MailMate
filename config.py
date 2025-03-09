import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GENAI_API_KEY")
genai.configure(api_key=api_key)
