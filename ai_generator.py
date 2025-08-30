import openai
import requests
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_image(prompt, save_path="image.png"):
    # New v1 method
    response = openai.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )
    
    image_url = response.data[0].url

    # Download the image
    img_data = requests.get(image_url).content
    with open(save_path, 'wb') as f:
        f.write(img_data)

    return save_path
