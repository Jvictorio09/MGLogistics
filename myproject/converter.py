from PIL import Image
import os

input_folder = r"C:\Users\ADMIN\Downloads\MGLogistics\myproject\myapp\static\img\bg"
output_folder = os.path.join(input_folder, "converted_dualtone_globe")
os.makedirs(output_folder, exist_ok=True)

# Color definitions
soft_dark_navy = (26, 31, 38)
navy = (0, 38, 77)

def close_color_match(color, target, tolerance=50):
    return all(abs(c - t) < tolerance for c, t in zip(color, target))

def is_red_or_orange(r, g, b):
    # Loosely detect red and orange tones
    return (r > 180 and g < 100 and b < 100) or (r > 200 and g > 100 and b < 50)

def transform_pixel(r, g, b, a):
    if a == 0:
        return (0, 0, 0, 0)
    elif (r, g, b) == (0, 0, 0):
        return (*soft_dark_navy, a)
    elif is_red_or_orange(r, g, b):
        return (*navy, a)
    else:
        return (r, g, b, a)

def transform_image(img):
    img = img.convert("RGBA")
    new_pixels = [transform_pixel(r, g, b, a) for (r, g, b, a) in img.getdata()]
    img.putdata(new_pixels)
    return img

# Batch convert
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                result = transform_image(img)
                result.save(output_path)
                print(f"🌍 Processed: {filename}")
        except Exception as e:
            print(f"❌ Error on {filename}: {e}")
