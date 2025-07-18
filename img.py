import os
import argparse
from PIL import Image

#!/usr/bin/env python3

"""
img_optimizer: Optimize and resize images in a directory.

Usage:
    python img.py --optimize 80 --width 800 --height 600 --directory /path/to/images

Dependencies:
    - Pillow

Install dependencies:
    pip install -r requirements.txt

This script will process all images in the specified directory, resize and optimize them,
and save the results in a subdirectory named "optimized".
"""


def optimize_images(optimize, width, height, directory):
    output_dir = os.path.join(directory, "optimized")
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if not os.path.isfile(file_path):
            continue
        try:
            with Image.open(file_path) as img:
                img = img.convert("RGB")
                # Preserve aspect ratio if only width or only height is provided
                orig_width, orig_height = img.width, img.height
                if width is not None and height is not None:
                    target_width, target_height = width, height
                elif width is not None:
                    aspect_ratio = orig_height / orig_width
                    target_width = width
                    target_height = int(width * aspect_ratio)
                elif height is not None:
                    aspect_ratio = orig_width / orig_height
                    target_height = height
                    target_width = int(height * aspect_ratio)
                else:
                    target_width, target_height = orig_width, orig_height
                img = img.resize((target_width, target_height), Image.LANCZOS)
                output_path = os.path.join(output_dir, filename)
                img.save(
                    output_path,
                    optimize=True,
                    quality=optimize
                )
                print(f"Optimized: {filename} -> {output_path}")
        except Exception as e:
            print(f"Skipping {filename}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Optimize and resize images in a directory.")
    parser.add_argument("-o", "--optimize", type=int, default=70, help="Optimization quality percentage (1-100), default: 70")
    parser.add_argument("-w", "--width", type=int, default=None, help="Target width (default: original image width)")
    parser.add_argument("-H", "--height", type=int, default=None, help="Target height (default: original image height)")
    parser.add_argument("-d", "--directory", type=str, required=True, help="Directory containing images")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print("Error: Directory does not exist.")
        return

    optimize_images(args.optimize, args.width, args.height, args.directory)

if __name__ == "__main__":
    main()