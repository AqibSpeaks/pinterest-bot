import openai
import requests
import os  # for reading environment variables

# Read the API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# If the key is missing, stop and show error
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in Streamlit secrets.")

openai.api_key = OPENAI_API_KEY

def generate_image(prompt, save_path="image.png"):
    response = openai.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )
    image_url = response.data[0].url

    img_data = requests.get(image_url).content
    with open(save_path, 'wb') as f:
        f.write(img_data)

    return save_path
