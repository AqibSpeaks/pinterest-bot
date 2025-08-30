import os
import openai
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in Streamlit secrets.")

openai.api_key = OPENAI_API_KEY
