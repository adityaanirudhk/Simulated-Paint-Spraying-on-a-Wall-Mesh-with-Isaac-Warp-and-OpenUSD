
import numpy as np
from PIL import Image

def save_texture(paint, filename):

    img = np.clip(paint,0,1)
    img = (img*255).astype(np.uint8)

    image = Image.fromarray(img)
    image = image.convert("L")

    image.save(filename)
