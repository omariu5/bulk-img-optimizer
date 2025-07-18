import os
import shutil
import tempfile
from PIL import Image
import pytest
from img import optimize_images

def create_test_image(path, size=(100, 100), color=(255, 0, 0)):
    img = Image.new("RGB", size, color)
    img.save(path, format="JPEG")

def test_optimize_images_creates_optimized_dir_and_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test images
        img1 = os.path.join(tmpdir, "test1.jpg")
        img2 = os.path.join(tmpdir, "test2.jpg")
        create_test_image(img1, (100, 200))
        create_test_image(img2, (300, 150))

        # Run optimizer (resize to 50x50)
        optimize_images(70, 50, 50, tmpdir)

        out_dir = os.path.join(tmpdir, "optimized")
        assert os.path.isdir(out_dir)
        out_files = os.listdir(out_dir)
        assert "test1.jpg" in out_files
        assert "test2.jpg" in out_files

        # Check output image size
        with Image.open(os.path.join(out_dir, "test1.jpg")) as out_img1:
            assert out_img1.size == (50, 50)
        with Image.open(os.path.join(out_dir, "test2.jpg")) as out_img2:
            assert out_img2.size == (50, 50)

def test_optimize_images_aspect_ratio_width_only():
    with tempfile.TemporaryDirectory() as tmpdir:
        img1 = os.path.join(tmpdir, "test1.jpg")
        create_test_image(img1, (200, 100))
        optimize_images(70, 100, None, tmpdir)
        out_dir = os.path.join(tmpdir, "optimized")
        with Image.open(os.path.join(out_dir, "test1.jpg")) as out_img:
            assert out_img.size == (100, 50)

def test_optimize_images_aspect_ratio_height_only():
    with tempfile.TemporaryDirectory() as tmpdir:
        img1 = os.path.join(tmpdir, "test1.jpg")
        create_test_image(img1, (100, 200))
        optimize_images(70, None, 100, tmpdir)
        out_dir = os.path.join(tmpdir, "optimized")
        with Image.open(os.path.join(out_dir, "test1.jpg")) as out_img:
            assert out_img.size == (50, 100)

def test_optimize_images_original_size():
    with tempfile.TemporaryDirectory() as tmpdir:
        img1 = os.path.join(tmpdir, "test1.jpg")
        create_test_image(img1, (123, 456))
        optimize_images(70, None, None, tmpdir)
        out_dir = os.path.join(tmpdir, "optimized")
        with Image.open(os.path.join(out_dir, "test1.jpg")) as out_img:
            assert out_img.size == (123, 456)
