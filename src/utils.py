"""
utils.py - Helper functions for the Face Recognition project
"""

import os
import cv2
import numpy as np


def load_image(image_path: str) -> np.ndarray:
    """Load an image from disk. Raises FileNotFoundError if not found."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image: {image_path}")
    return img


def resize_image(img: np.ndarray, width: int = 640) -> np.ndarray:
    """Resize image to a given width while maintaining aspect ratio."""
    h, w = img.shape[:2]
    ratio = width / w
    new_size = (width, int(h * ratio))
    return cv2.resize(img, new_size)


def list_images(folder: str, extensions=(".jpg", ".jpeg", ".png")) -> list:
    """Return all image file paths in a folder."""
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.lower().endswith(extensions)
    ]


def ensure_dir(path: str):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
