# Face Recognition Project

A Python-based face recognition system using **DeepFace** — covering both **face detection** and **face recognition** tasks.

## Face Recognition ≠ Face Classification
- **Face Detection** → Locate faces in an image (outputs bounding boxes)
- **Face Recognition** → Identify *who* the face belongs to

## Use Cases
- Face in Wildlife monitoring
- Cancer detection (medical imaging)
- General identity verification

---

## Project Structure

```
face-recognition-project/
├── data/
│   ├── raw/              # Original unprocessed images
│   ├── processed/        # Preprocessed images
│   └── known_faces/      # Reference images per person (one folder per identity)
├── src/
│   ├── detect.py         # Face detection module
│   ├── recognize.py      # Face recognition module
│   ├── utils.py          # Helper functions
│   └── pipeline.py       # End-to-end pipeline
├── models/               # Saved model weights (if any)
├── tests/                # Unit tests
├── results/              # Output images and logs
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/face-recognition-project.git
cd face-recognition-project
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Face Detection
```bash
python src/detect.py --image data/raw/sample.jpg
```

### Face Recognition
```bash
python src/recognize.py --image data/raw/sample.jpg --db data/known_faces/
```

### Full Pipeline
```bash
python src/pipeline.py --image data/raw/sample.jpg
```

---

## Requirements
- Python 3.8+
- DeepFace
- OpenCV
- See `requirements.txt` for full list

---

## License
MIT
