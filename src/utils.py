import glob
import os

def list_images(folder: str, extensions=("jpg", "jpeg", "png")):
    """
    List all image files inside a folder.
    """
    images = []
    for ext in extensions:
        images.extend(glob.glob(os.path.join(folder, f"*.{ext}")))
    return images
