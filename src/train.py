from ultralytics import YOLO
import os

def train_yolo_model(
    dataset_path: str,
    model_name: str = "yolov8n.pt",
    output_dir: str = None,
    epochs: int = 50,
    imgsz: int = 640,
    batch: int = 16,
):
    """
    Train a YOLOv8 model on a given dataset folder.
    Expects: train/, valid/, test/, and data.yaml inside dataset_path.
    """

    yaml_path = os.path.join(dataset_path, "data.yaml")
    if not os.path.exists(yaml_path):
        raise FileNotFoundError(f"data.yaml not found in {dataset_path}")

    output_dir = output_dir or os.path.join(dataset_path, "model")
    os.makedirs(output_dir, exist_ok=True)

    model = YOLO(model_name)
    results = model.train(
        data=yaml_path,
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,
        project=output
