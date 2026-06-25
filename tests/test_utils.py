"""
test_utils.py - Unit tests for utility functions
"""

import os
import sys
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from utils import resize_image, list_images, ensure_dir


def test_resize_image():
    img = np.zeros((480, 1280, 3), dtype=np.uint8)
    resized = resize_image(img, width=640)
    assert resized.shape[1] == 640
    assert resized.shape[0] == 240  # aspect ratio preserved


def test_list_images_empty(tmp_path):
    images = list_images(str(tmp_path))
    assert images == []


def test_ensure_dir(tmp_path):
    new_dir = str(tmp_path / "new_folder")
    ensure_dir(new_dir)
    assert os.path.isdir(new_dir)


def test_load_image_not_found():
    from utils import load_image
    with pytest.raises(FileNotFoundError):
        load_image("nonexistent.jpg")
