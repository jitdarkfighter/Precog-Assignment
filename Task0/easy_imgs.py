
import os
import csv
import random
import string
from PIL import Image, ImageDraw, ImageFont


output_dir = 'Task0/captcha_images/easy'
os.makedirs(output_dir, exist_ok=True)
Image_size = (200, 80)
font_size = 40
num_samples = 100
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

with open('Task0/ai_wordlist.txt', 'r') as f:
    words = [line.strip() for line in f.readlines()]


output_file_path = os.path.join(output_dir, 'labels.csv')
i = 0
with open(output_file_path, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['filename', 'label'])

    print(len(words))
    for word in words:
        image = Image.new('RGB', Image_size, (255, 255, 255))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font_path, font_size)

        bbox = draw.textbbox((0, 0), word, font=font)
        text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        position = ((Image_size[0]-text_w)//2, (Image_size[1]-text_h)//2)
        draw.text(position, word, fill="black", font = font)
        filename = f"img_{i}.png"
        i+= 1
        image.save(os.path.join(output_dir, filename))
        writer.writerow([filename, word])

