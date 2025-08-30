import os
import numpy as np
import csv 
import random
import string
from PIL import Image, ImageDraw, ImageFont

train_output_dir = 'Task2/captcha_images/train/hard'
test_output_dir = 'Task2/captcha_images/test/hard'
os.makedirs(train_output_dir, exist_ok=True)
os.makedirs(test_output_dir, exist_ok=True)
image_size = (200,80)
font_size = 40
num_samples = 100


font_dir = "/usr/share/fonts/TTF"
font_paths = [os.path.join(font_dir, font) for font in os.listdir(font_dir) if font.endswith(".ttf")]

def generate_random_word():
    length = random.randint(5, 8)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

num_words = 500
words = [generate_random_word() for _ in range(num_words)]


def add_noise(image):
    np_img = np.array(image).astype(np.int16)
    noise = np.random.normal(0, 50, np_img.shape) 
    noisy = np.clip(np_img + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy)


def random_caps(word):
    return ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in word)


def get_font(font_paths = font_paths):
    return random.choice(font_paths)

# training images
output_file_path = os.path.join("Task2/captcha_images/train", 'labels_hard.csv')
i = 0
with open(output_file_path, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['filename', 'label'])

    print(len(words))
    for word in words:
        # 50 train images for each word
        for num_samples in range(50):
            font_path = get_font()
            word = random_caps(word)
            image = Image.new('RGB', image_size, (255, 255, 255))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(font_path, font_size)

            bbox = draw.textbbox((0, 0), word, font=font)
            text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            position = ((image_size[0]-text_w)//2, (image_size[1]-text_h)//2)

            # Random rgb text color,which is suitable with white background
            text_color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
            draw.text(position, word, fill=text_color, font=font)

            image = add_noise(image)

            filename = f"img_{i}.png"
            i+= 1
            image.save(os.path.join(train_output_dir, filename))
            writer.writerow([filename, word])

# Test images
output_file_path = os.path.join('Task2/captcha_images/test', 'labels_hard.csv')
i = 0
with open(output_file_path, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['filename', 'label'])

    for word in words:
        # 15 images for each word in test dataset.
        for num_samples in range(15):
            font_path = get_font()
            word = random_caps(word)
            image = Image.new('RGB', image_size, (255, 255, 255))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(font_path, font_size)

            bbox = draw.textbbox((0, 0), word, font=font)
            text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            position = ((image_size[0]-text_w)//2, (image_size[1]-text_h)//2)

            # Random rgb text color,which is suitable with white background
            text_color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
            draw.text(position, word, fill=text_color, font=font)

            image = add_noise(image)

            filename = f"img_{i}.png"
            i+= 1
            image.save(os.path.join(test_output_dir, filename))
            writer.writerow([filename, word])
