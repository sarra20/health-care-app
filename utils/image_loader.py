import os

def validate_image(image_path):

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image non trouvée: {image_path}")

    valid_extensions = [".jpg", ".jpeg", ".png"]

    ext = os.path.splitext(image_path)[1].lower()

    if ext not in valid_extensions:
        raise ValueError("Format d'image non supporté")

    return image_path