"""
detect.py - Face Detection using DeepFace
Finds face locations (bounding boxes) in an image.
"""

import argparse
import cv2
from deepface import DeepFace


def detect_faces(image_path: str, detector_backend: str = "opencv") -> list:
    """
    Detect faces in an image and return bounding boxes.

    Args:
        image_path: Path to the input image.
        detector_backend: Detection backend ('opencv', 'retinaface', 'mtcnn', 'ssd').

    Returns:
        List of dicts with keys: 'x', 'y', 'w', 'h', 'confidence'.
    """
    face_objs = DeepFace.extract_faces(
        img_path=image_path,
        detector_backend=detector_backend,
        enforce_detection=False,
    )

    results = []
    for face in face_objs:
        region = face.get("facial_area", {})
        results.append({
            "x": region.get("x", 0),
            "y": region.get("y", 0),
            "w": region.get("w", 0),
            "h": region.get("h", 0),
            "confidence": face.get("confidence", 0.0),
        })

    print(f"[detect] Found {len(results)} face(s) in '{image_path}'")
    return results


def draw_boxes(image_path: str, faces: list, output_path: str = "results/detected.jpg"):
    """Draw bounding boxes on the image and save."""
    img = cv2.imread(image_path)
    for face in faces:
        x, y, w, h = face["x"], face["y"], face["w"], face["h"]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        label = f"{face['confidence']:.2f}"
        cv2.putText(img, label, (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    cv2.imwrite(output_path, img)
    print(f"[detect] Saved output to '{output_path}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Face Detection")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--backend", default="opencv", help="Detector backend")
    parser.add_argument("--output", default="results/detected.jpg", help="Output path")
    args = parser.parse_args()

    faces = detect_faces(args.image, args.backend)
    draw_boxes(args.image, faces, args.output)
