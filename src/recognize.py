"""
recognize.py - Face Recognition using DeepFace
Identifies faces by comparing against a database of known faces.
"""

import argparse
import os
import cv2
from deepface import DeepFace


def recognize_faces(
    image_path: str,
    db_path: str,
    model_name: str = "VGG-Face",
    distance_metric: str = "cosine",
    detector_backend: str = "opencv",
) -> list:
    """
    Recognize faces in an image against a known-faces database.

    Args:
        image_path:       Path to the input image.
        db_path:          Path to the folder of known faces (one subfolder per person).
        model_name:       Recognition model ('VGG-Face', 'Facenet', 'ArcFace', etc.).
        distance_metric:  Similarity metric ('cosine', 'euclidean', 'euclidean_l2').
        detector_backend: Detection backend to use.

    Returns:
        List of recognition result dicts.
    """
    if not os.path.isdir(db_path):
        raise FileNotFoundError(f"Known-faces database not found: {db_path}")

    results = DeepFace.find(
        img_path=image_path,
        db_path=db_path,
        model_name=model_name,
        distance_metric=distance_metric,
        detector_backend=detector_backend,
        enforce_detection=False,
    )

    identities = []
    for df in results:
        if not df.empty:
            top = df.iloc[0]
            identity = os.path.basename(os.path.dirname(top["identity"]))
            identities.append({
                "identity": identity,
                "distance": round(top[f"{model_name}_{distance_metric}"], 4),
                "image": top["identity"],
            })
            print(f"[recognize] Matched → {identity} (distance: {identities[-1]['distance']})")
        else:
            identities.append({"identity": "Unknown", "distance": None, "image": None})
            print("[recognize] No match found → Unknown")

    return identities


def verify_faces(image1_path: str, image2_path: str, model_name: str = "VGG-Face") -> dict:
    """
    Verify whether two images contain the same person.

    Args:
        image1_path: Path to first image.
        image2_path: Path to second image.
        model_name:  Recognition model to use.

    Returns:
        Dict with 'verified' (bool) and 'distance' (float).
    """
    result = DeepFace.verify(
        img1_path=image1_path,
        img2_path=image2_path,
        model_name=model_name,
        enforce_detection=False,
    )
    print(f"[verify] Same person: {result['verified']} | Distance: {result['distance']:.4f}")
    return {"verified": result["verified"], "distance": result["distance"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Face Recognition")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--db", required=True, help="Path to known-faces database folder")
    parser.add_argument("--model", default="VGG-Face", help="Recognition model")
    parser.add_argument("--metric", default="cosine", help="Distance metric")
    args = parser.parse_args()

    recognize_faces(args.image, args.db, args.model, args.metric)
