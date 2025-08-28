# Image Resizer

## Overview
This Python script resizes images in a specified folder to a user-defined size and saves them to an output folder. It uses the PIL (Python Imaging Library) module to handle image processing and supports common image formats like JPG, PNG, BMP, GIF, and TIFF.

## Features
- Resizes all supported images in a given folder to a specified width and height.
- Allows users to specify an input folder containing images.
- Optionally allows users to specify an output folder; if not provided, creates a "resized" subfolder in the input folder.
- Supports multiple image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`.
- Uses the LANCZOS resampling method for high-quality resizing.
- Skips non-image files and handles errors gracefully.

## Requirements
- Python 3.x
- Pillow (PIL) library
  Install it using:
  ```bash
  pip install Pillow
  ```

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Follow the prompts:
   - Enter the path to the folder containing the images.
   - Enter the path for the output folder (or press Enter to create a "resized" folder inside the input folder).
   - Enter the desired size in the format `WIDTHxHEIGHT` (e.g., `512x512`). If invalid, defaults to 512x512.
3. The script will process all supported images in the input folder, resize them, and save them to the output folder.

## Example
```bash
Enter the path to the folder with images: /path/to/images
Enter the path to the folder for resized images (press Enter to auto-create inside input folder): 
Enter size in format WIDTHxHEIGHT (e.g. 512x512): 256x256
Saved: /path/to/images/resized/image1.jpg
Saved: /path/to/images/resized/image2.png
Skipped invalid_image.txt: Not an image file
```

## Notes
- Ensure the input folder exists and contains supported image files.
- The script creates the output folder if it doesn't exist.
- Non-image files in the input folder are skipped.
- If an image cannot be processed (e.g., corrupted file), the script will print an error and continue with the next file.

## License
This project is licensed under the MIT License.