import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

OUTPUT_DIR = "output"

def generate_captcha(hard=False):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    x = random.randint(10, 99)
    y = random.randint(10, 99)
    z = random.randint(10, 99)

    operators = ['+', '-', '*', '/']
    op1 = random.choice(operators)
    op2 = random.choice(operators)

    equation = f"{x} {op1} {y} {op2} {z}"

    img = Image.new('RGB', (250, 70), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()

    draw.text((20, 20), equation, fill=(0, 0, 0), font=font)

    if hard:
        img = add_distortions(img)

    captcha_path = os.path.join(OUTPUT_DIR, "captcha.png")
    img.save(captcha_path)
    
    print(f"Captcha generated: {equation} (Saved at {captcha_path})")
    return equation, captcha_path

def add_distortions(img):
    draw = ImageDraw.Draw(img)

    # Add random lines
    for _ in range(5):
        x1 = random.randint(0, img.width)
        y1 = random.randint(0, img.height)
        x2 = random.randint(0, img.width)
        y2 = random.randint(0, img.height)
        draw.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=2)

    # Add random dots
    for _ in range(100):
        x = random.randint(0, img.width)
        y = random.randint(0, img.height)
        draw.point((x, y), fill=(0, 0, 0))

    # Apply blur
    img = img.filter(ImageFilter.GaussianBlur(1))

    return img

