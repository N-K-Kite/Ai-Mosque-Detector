# Ai-Mosque-Detector
An Ai model i built that detects mosques ( for now ) and displays DO NOT ENGAGE in ( drone, warship , aircraft ) aerial imagery , and prevents them from engaging said location in accordance with IHL, unless provided with an authorization from TOC.


## 🎯 Project Goals
- Prevent accidental strikes on religious structures
- Enable safe autonomous drone operations
- Comply with IHL principles of distinction and proportionality
- Provide real-time protected zone identification

## 🛠️ Technology Stack
- **Model**: YOLOv5s (fine-tuned)
- **Framework**: PyTorch, Ultralytics
- **Training**: Google Colab (Tesla T4 GPU)
- **Dataset**: 492 annotated mosque images
- **Language**: Python 3.12

## 📊 Performance
- **Accuracy (mAP50)**: 98.9%
- **Precision**: 84.3%
- **Recall**: 98.0%
- **Inference Speed**: ~10ms per image

## 🚀 Quick Start

### Installation
```bash
pip install ultralytics torch pillow
```

### Usage
```python
from ultralytics import YOLO

# Load trained model
model = YOLO('best.pt')

# Detect mosques in image
results = model('drone_image.jpg', conf=0.5)

# Check if protected zone
if len(results[0].boxes) > 0:
    print("⚠️  Protected zone detected - DO NOT ENGAGE")
else:
    print("✅ Area clear")
```

## 📁 Project Structure
```
mosque-detector/
├── best.pt                 # Trained model weights
├── notebook.ipynb          # Training notebook
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## 🎓 Academic Context
This project was developed as a late night passtime exploring the application of computer vision and deep learning in humanitarian technology and conflict resolution.

## 🔮 Future Work
- Expand detection to hospitals, schools, cultural sites
- Implement multi-class detection system
- Deploy to edge devices (NVIDIA Jetson)
- Real-time video stream processing
- Integration with drone autopilot systems

## 📄 License
MIT License - Free for humanitarian and educational use

## 🤝 Acknowledgments
- Dataset: Roboflow Universe
- Framework: Ultralytics YOLOv5
- Training Platform: Google Colab

---
**Note**: This system is designed for humanitarian applications. The conservative bounding box approach prioritizes safety by creating larger no-engagement zones around protected structures.
