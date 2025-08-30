from ai_generator import generate_image
from pinterest_bot import post_to_pinterest
import random

# List of keywords for pins
keywords = ['home office decor', 'minimalist living room', 'kitchen organization', 'modern workspace', 'living room ideas']

def run_daily_post():
    keyword = random.choice(keywords)
    image_path = generate_image(keyword)
    title = f"{keyword} Ideas"
    description = f"Discover amazing {keyword} tips!"
    post_to_pinterest(image_path, title, description)

if __name__ == "__main__":
    run_daily_post()
