# main.py or ai_generator.py
import streamlit as st
import openai
import requests

# 1️⃣ Set OpenAI API key from Streamlit secrets
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

# 2️⃣ Function to generate an image using OpenAI
def generate_image(prompt, save_path="image.png"):
    response = openai.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )
    image_url = response.data[0].url

    # Download the image locally
    img_data = requests.get(image_url).content
    with open(save_path, "wb") as f:
        f.write(img_data)

    return save_path

# 3️⃣ Streamlit UI (example)
st.title("Pinterest AI Image Bot")
prompt = st.text_input("Enter image prompt")
if st.button("Generate Image"):
    image_path = generate_image(prompt)
    st.image(image_path)
