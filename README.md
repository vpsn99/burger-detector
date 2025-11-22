# Burger Detector

Teaching Your Laptop to Spot Burgers: Training a YOLOv8 Model From Scratch

This repository contains code and instructions for training a custom YOLOv8 object detection model that identifies **burgers** in images.  
It demonstrates dataset preparation, annotation, model training, inference, and visualization.

## Features
- YOLOv8-based custom object detector  
- Modular Python training and inference scripts  
- Jupyter/Colab notebook included  
- Easily extendable to new object categories  
- Clean GitHub-friendly structure  

## Project Structure
```
burger-detector/
│
├── notebooks/                # Jupyter/Colab notebooks
├── src/                      # Python modules
│   ├── train.py
│   ├── inference.py
│   ├── visualize.py
│   └── utils.py
│
├── data/                     # Dataset placeholder (no actual images)
│   └── README.md
│
├── requirements.txt
└── LICENSE
```

## Train Your Own Model

```python
from src.train import train_yolo_model

train_yolo_model(
    dataset_path="data/",
    model_name="yolov8s.pt",
    epochs=50,
    imgsz=640,
    batch=16
)
```

## Inference Example

```python
from src.inference import load_model, run_inference
from src.visualize import show_side_by_side

model = load_model("path/to/best.pt")
results = run_inference(model, "image.jpg", conf=0.25)
show_side_by_side("image.jpg", results)
```

## Dataset Not Included
This repo does **not** include training images due to potential copyright restrictions.  
Refer to `data/README.md` for instructions on preparing your own dataset.

## License
This project is released under the MIT License.

## Author
GitHub: https://github.com/vpsn99
