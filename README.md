# Python Image Optimizer

This script optimizes and resizes all images in a specified directory using Pillow, saving the results in a subdirectory named `optimized`.

## Features
- Resize images to a specified width and height
- Optimize image quality
- Supports batch processing of all images in a directory

## Requirements
- Python 3.11+
- Pillow (see `requirements.txt`)

## Installation
1. Clone this repository or download the script.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script from the command line:


```sh
python img.py -d /path/to/images [-o 80] [-w 800] [-H 600]
```

- `-d`, `--directory` : Directory containing images (**required**)
- `-o`, `--optimize`  : Optimization quality percentage (1-100, default: 70)
- `-w`, `--width`     : Target width (default: original image width)
- `-H`, `--height`    : Target height (default: original image height)



If width and height are not specified, the original image size is used.

**Aspect Ratio:**
- If only width is provided, the height is automatically calculated to preserve the original aspect ratio.
- If only height is provided, the width is automatically calculated to preserve the original aspect ratio.
- If both width and height are provided, the image is resized to those exact dimensions (aspect ratio may change).

The optimized images will be saved in a subdirectory called `optimized` inside the specified directory.

## Example


```sh
# Only directory required, uses defaults for optimize, width, and height
python img.py -d ./images

# With custom optimization and resizing
python img.py -d ./images -o 75 -w 1024 -H 768

# Preserve aspect ratio by specifying only width
python img.py -d ./images -w 800

# Preserve aspect ratio by specifying only height
python img.py -d ./images -H 600
```

## Donate

If you find this project useful, consider supporting it:

<a href="http://paypal.me/omariu5" target="_blank">
  <img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="Donate with PayPal button" />
</a>

## License
MIT License
