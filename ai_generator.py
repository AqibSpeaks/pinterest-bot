import openai
import requests
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_image(prompt, save_path="image.png"):
    # Use the compatible endpoint
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    # Download the image
    img_data = requests.get(image_url).content
    with open(save_path, 'wb') as f:
        f.write(img_data)

    return save_path
