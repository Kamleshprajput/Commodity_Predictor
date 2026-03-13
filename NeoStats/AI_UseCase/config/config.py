import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
MODEL_NAME = "gemini-2.5-flash"
