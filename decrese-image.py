from PIL import Image
from pathlib import Path
import os.path

folder_with_images = Path("C:/Users/.Michal/Desktop/")
folder_for_reduced_images = Path("C:/Users/.Michal/Desktop/reduced/")

valid_images = [".jpg", ".gif", ".png", ".tga"]

for path, subdirs, files in os.walk(folder_with_images):
    for name in files:
        file_path = os.path.join(path, name)
        filename = Path(file_path).stem
        extension = os.path.splitext(file_path)[1]
        if extension.lower() not in valid_images:
            continue

        image = Image.open(os.path.join(folder_with_images, file_path))
        if image.mode in ("RGBA", "P"): 
            image = image.convert("RGB")
        reducedImage = image.resize((100, 100), Image.ANTIALIAS)
        reducedImage.save(folder_for_reduced_images /
                      (filename + ".jpg"), quality=100)