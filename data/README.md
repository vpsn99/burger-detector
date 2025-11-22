# Dataset Placeholder

The training dataset is **not included** in this repository due to copyright and licensing concerns.

To train your model, prepare your dataset in the following structure:

```
data/
    train/
        images/
        labels/
    valid/
        images/
        labels/
    test/
        images/
        labels/
    data.yaml
```

## Steps to Prepare Your Dataset

1. Collect or download images containing the objects you want to detect.
2. Annotate them using a tool such as **Roboflow**, **LabelImg**, or **CVAT**.
3. Export the dataset in **YOLOv8 format**.
4. Place the images and label files into the appropriate folders above.
5. Update `data.yaml` so that paths match this folder structure.

Example `data.yaml`:

```yaml
train: data/train/images
val: data/valid/images
test: data/test/images

nc: 1
names: ["burger"]
```

## Important
Do **not** commit copyrighted images into the repository.  
Keep your dataset local to your machine or cloud workspace.

