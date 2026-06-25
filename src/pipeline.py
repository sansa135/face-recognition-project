"""
pipeline.py - End-to-end Face Detection + Recognition Pipeline
"""

import argparse
import os
from detect import detect_faces, draw_boxes
from recognize import recognize_faces


def run_pipeline(image_path: str, db_path: str, output_dir: str = "results"):
    """
    Full pipeline: detect faces then recognize each one.

    Args:
        image_path: Path to input image.
        db_path:    Path to known-faces database.
        output_dir: Directory to save results.
    """
    os.makedirs(output_dir, exist_ok=True)

    print("\n=== Step 1: Face Detection ===")
    faces = detect_faces(image_path)
    output_path = os.path.join(output_dir, "detected.jpg")
    draw_boxes(image_path, faces, output_path)

    print("\n=== Step 2: Face Recognition ===")
    if db_path and os.path.isdir(db_path):
        identities = recognize_faces(image_path, db_path)
        for i, result in enumerate(identities):
            print(f"  Face {i+1}: {result['identity']} (distance: {result['distance']})")
    else:
        print("  No database provided — skipping recognition.")

    print(f"\n=== Done! Results saved to '{output_dir}/' ===")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Face Recognition Pipeline")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--db", default="data/known_faces", help="Known-faces database path")
    parser.add_argument("--output", default="results", help="Output directory")
    args = parser.parse_args()

    run_pipeline(args.image, args.db, args.output)
