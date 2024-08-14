import numpy
import imagehash
from PIL import Image, ImageFilter

IMAGE_FILE = '../examples/mrbean.png'
image = Image.open(IMAGE_FILE)

hash = imagehash.phash(image, 16)
print(hash)
print(len(str(hash)))