import os
from PIL import Image

# Ask user for input folder
input_folder = input("Enter the path to the folder with images: ").strip('"')

# Ask user for output folder (optional)
output_folder = input("Enter the path to the folder for resized images (press Enter to auto-create inside input folder): ").strip('"')

# If skipped → create "resized" inside input folder
if not output_folder:
    output_folder = os.path.join(input_folder, "resized")

# Ask user for size
size_str = input("Enter size in format WIDTHxHEIGHT (e.g. 512x512): ")
try:
    width, height = map(int, size_str.lower().split("x"))
except Exception:
    print("Invalid format. Defaulting to 512x512.")
    width, height = 512, 512

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Supported image formats
valid_ext = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")

for filename in os.listdir(input_folder):
    if not filename.lower().endswith(valid_ext):
        continue  # skip non-image files

    input_path = os.path.join(input_folder, filename)
    try:
        with Image.open(input_path) as img:
            img_resized = img.resize((width, height), Image.LANCZOS)
            output_path = os.path.join(output_folder, filename)
            img_resized.save(output_path)
            print(f"Saved: {output_path}")
    except Exception as e:
        print(f"Skipped {filename}: {e}")
