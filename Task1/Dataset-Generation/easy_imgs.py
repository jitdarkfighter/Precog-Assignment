
import os
import csv
import random
import string
from PIL import Image, ImageDraw, ImageFont


train_output_dir = 'Task1/captcha_images/train/easy'
test_output_dir = 'Task1/captcha_images/test/easy'
os.makedirs(train_output_dir, exist_ok=True)
os.makedirs(test_output_dir, exist_ok=True)

Image_size = (200, 80)
font_size = 40
num_samples = 100
train_font_paths = [
    '/usr/share/fonts/liberation/LiberationSans-Regular.ttf',
    '/usr/share/fonts/liberation/LiberationSerif-Regular.ttf', 
    '/usr/share/fonts/liberation/LiberationMono-Regular.ttf',
    '/usr/share/fonts/TTF/DejaVuSerif-Bold.ttf',
    '/usr/share/fonts/TTF/DejaVuSans-Oblique.ttf',
]

test_font_paths = [
    '/usr/share/fonts/TTF/DejaVuSansCondensed-Bold.ttf',
    '/usr/share/fonts/noto/NotoSans-Regular.ttf',
    '/usr/share/fonts/noto/NotoSerif-Regular.ttf'
]

with open('Task0/ai_wordlist.txt', 'r') as f:
    words = [line.strip() for line in f.readlines()]


#Train datasets
output_file_path = os.path.join("Task1/captcha_images/train", 'labels_easy.csv')
i = 0
with open(output_file_path, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['filename', 'label'])

    print(len(words))
    for word in words:
        for font_path in train_font_paths:
            image = Image.new('RGB', Image_size, (255, 255, 255))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(font_path, font_size)

            bbox = draw.textbbox((0, 0), word, font=font)
            text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            position = ((Image_size[0]-text_w)//2, (Image_size[1]-text_h)//2)
            draw.text(position, word, fill="black", font = font)
            filename = f"img_{i}.png"
            i+= 1
            image.save(os.path.join(train_output_dir, filename))
            writer.writerow([filename, word])

#Test Datasets
output_file_path = os.path.join("Task1/captcha_images/test", 'labels_easy.csv')
i = 0
with open(output_file_path, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['filename', 'label'])

    for word in words:
        for font_path in test_font_paths:
            image = Image.new('RGB', Image_size, (255, 255, 255))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(font_path, font_size)

            bbox = draw.textbbox((0, 0), word, font=font)
            text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            position = ((Image_size[0]-text_w)//2, (Image_size[1]-text_h)//2)
            draw.text(position, word, fill="black", font = font)
            filename = f"img_{i}.png"
            i+= 1
            image.save(os.path.join(test_output_dir, filename))
            writer.writerow([filename, word])
