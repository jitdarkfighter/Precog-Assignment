import os
import numpy as np
import csv 
import random
import string
from PIL import Image, ImageDraw, ImageFont


output_dir = 'Task0/captcha_images/bonus'
os.makedirs(output_dir, exist_ok=True)
image_size = (250,100)
font_size = 40
num_samples = 100

# Extended font list with 11 working fonts for more diversity
font_paths = [
    '/usr/share/fonts/liberation/LiberationSans-Regular.ttf',
    '/usr/share/fonts/liberation/LiberationSerif-Regular.ttf', 
    '/usr/share/fonts/liberation/LiberationMono-Regular.ttf',
    '/usr/share/fonts/TTF/DejaVuSerif-Bold.ttf',
    '/usr/share/fonts/TTF/DejaVuSans-Oblique.ttf',
    '/usr/share/fonts/TTF/DejaVuSansCondensed-Bold.ttf',
    '/usr/share/fonts/noto/NotoSans-Regular.ttf',
    '/usr/share/fonts/noto/NotoSerif-Regular.ttf'
]

with open('Task0/ai_wordlist.txt', 'r') as f:
    words = [line.strip() for line in f.readlines()]


def add_noise(image):
    np_img = np.array(image).astype(np.int16)
    # Reduced noise for colored backgrounds
    noise = np.random.normal(0, 15, np_img.shape) 
    noisy = np.clip(np_img + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy)


def random_caps(word):
    return ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in word)


def get_font(font_paths = font_paths):
    return random.choice(font_paths)

def generate_dataset(writer):
    i = 0
    print(len(words))
    for word in words:
        font_path = get_font()
        word = random_caps(word)
        original_word = word
        for bg_color in ['green','red']:
            if bg_color == 'red':
                bg_color_val = (255, 0, 0)
                word = word[::-1]
            else:
                bg_color_val = (0, 255, 0)
            image = Image.new('RGB', image_size, bg_color_val)
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(font_path, font_size)

            bbox = draw.textbbox((0, 0), word, font=font)
            text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            position = ((image_size[0]-text_w)//2, (image_size[1]-text_h)//2)
            
            draw.text(position, word, fill=50, font=font)

            image = add_noise(image)

            filename = f"img_{bg_color}_{i}.png"
            i+= 1
            image.save(os.path.join(output_dir, filename))
            writer.writerow([filename, original_word])



output_file_path = os.path.join(output_dir, 'labels.csv')
with open(output_file_path, mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['filename', 'label'])

        generate_dataset(writer)
             

