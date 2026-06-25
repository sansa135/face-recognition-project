<div align="center">

<!-- Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1a2e,100:16213e&height=200&section=header&text=Face%20Recognition%20Project&fontSize=42&fontColor=58a6ff&fontAlignY=38&desc=Powered%20by%20DeepFace%20%7C%20Python&descAlignY=58&descColor=8b949e" width="100%"/>

<!-- Badges -->
<p>
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/DeepFace-0.0.79%2B-FF6B6B?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-4.8%2B-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
</p>

<p>
  <img src="https://img.shields.io/github/stars/sansa135/face-recognition-project?style=social"/>
  &nbsp;
  <img src="https://img.shields.io/github/forks/sansa135/face-recognition-project?style=social"/>
</p>

</div>

---

## 🧠 What is this?

> **Face Recognition ≠ Face Classification**

This project implements a complete **face analysis pipeline** using the power of [DeepFace](https://github.com/serengil/deepface) — one of the most accurate deep learning facial analysis frameworks.

| Task | Description | Output |
|------|-------------|--------|
| 🔍 **Face Detection** | Locate faces in an image | Bounding boxes |
| 🧬 **Face Recognition** | Identify *who* the face belongs to | Identity match |

---

## ✨ Use Cases

<table>
  <tr>
    <td align="center">🐾<br/><b>Wildlife Monitoring</b><br/>Track animals using facial patterns</td>
    <td align="center">🏥<br/><b>Cancer Detection</b><br/>Medical imaging analysis</td>
    <td align="center">🔐<br/><b>Identity Verification</b><br/>Secure authentication systems</td>
  </tr>
</table>

---

## 📁 Project Structure

```
face-recognition-project/
│
├── 📂 data/
│   ├── raw/                  # Original unprocessed images
│   ├── processed/            # Preprocessed images
│   └── known_faces/          # Reference images (one subfolder per identity)
│
├── 📂 src/
│   ├── detect.py             # 🔍 Face detection module
│   ├── recognize.py          # 🧬 Face recognition & verification
│   ├── pipeline.py           # 🚀 End-to-end pipeline
│   └── utils.py              # 🛠️  Helper functions
│
├── 📂 models/                # Saved model weights
├── 📂 tests/                 # Unit tests
├── 📂 results/               # Output images and logs
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚡ Quick Start

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sansa135/face-recognition-project.git
cd face-recognition-project
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 🔍 Face Detection
```bash
python src/detect.py --image data/raw/sample.jpg
```

### 🧬 Face Recognition
```bash
python src/recognize.py --image data/raw/sample.jpg --db data/known_faces/
```

### 🔄 Full Pipeline
```bash
python src/pipeline.py --image data/raw/sample.jpg --db data/known_faces/
```

---

## 🤖 Supported Models

| Model | Type | Speed | Accuracy |
|-------|------|-------|----------|
| `VGG-Face` | Recognition | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| `Facenet` | Recognition | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| `ArcFace` | Recognition | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| `RetinaFace` | Detection | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| `MTCNN` | Detection | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 📦 Requirements

```
deepface >= 0.0.79
opencv-python >= 4.8.0
numpy >= 1.24.0
pandas >= 2.0.0
matplotlib >= 3.7.0
Pillow >= 10.0.0
tqdm >= 4.65.0
```

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by [sansa135](https://github.com/sansa135)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:16213e,50:1a1a2e,100:0d1117&height=100&section=footer" width="100%"/>

</div>
