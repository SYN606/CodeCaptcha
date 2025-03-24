import random
from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = "output"

def generate_captcha():
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    
    x = random.randint(10, 99)
    y = random.randint(10, 99)
    z = random.randint(10, 99)

    
    operators = ['+', '-', '*', '/']
    op1 = random.choice(operators)
    op2 = random.choice(operators)

    
    equation = f"{x} {op1} {y} {op2} {z}"

    # Create an image with white background
    img = Image.new('RGB', (250, 70), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Load font (uses a default one if Arial is missing)
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()

    
    draw.text((20, 20), equation, fill=(0, 0, 0), font=font)

    
    captcha_path = os.path.join(OUTPUT_DIR, "captcha.png")
    img.save(captcha_path)
    
    print(f"Captcha generated: {equation} (Saved at {captcha_path})")
    return equation, captcha_path

