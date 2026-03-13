import os
import sys
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from config.config import GEMINI_API_KEY, MODEL_NAME
load_dotenv()
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def get_gemini_model():
    """Initialize and return the gemini chat model"""
    try:
        # Initialize the Google chat model with the API key
        gemini_model = ChatGoogleGenerativeAI(
            api_key=GEMINI_API_KEY,
            model=MODEL_NAME,
            temperature=0.3,
        )
        return gemini_model
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Gemini model: {str(e)}")