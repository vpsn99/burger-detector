from PIL import Image
import matplotlib.pyplot as plt

def show_side_by_side(original_path: str, results):
    """
    Displays original image and YOLO-predicted output side by side.
    """
    original = Image.open(original_path)

    # Save YOLO inference output temporarily
    results[0].save("temp_pred.jpg")
    predicted = Image.open("temp_pred.jpg")

    plt.figure(figsize=(12, 6))

    # left: original
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(original)
    plt.axis("off")

    # right: prediction
    plt.subplot(1, 2, 2)
    plt.title("Prediction")
    plt.imshow(predicted)
    plt.axis("off")

    plt.tight_layout()
    plt.show()
