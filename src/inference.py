from ultralytics import YOLO
import os

def load_model(weights_path: str):
    """
    Load YOLO model from a given weights (.pt) file.
    """
    if not os.path.exists(weights_path):
        raise FileNotFoundError(f"Weights not found at: {weights_path}")
    return YOLO(weights_path)

def run_inference(model, image_path: str, save: bool = False, conf: float = 0.25):
    """
    Run YOLO inference on a single image.
    """
    return model(image_path, save=save, conf=conf)
