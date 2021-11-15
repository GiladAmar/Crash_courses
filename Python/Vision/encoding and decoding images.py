import numpy as np
import base64
from PIL import Image
from io import BytesIO

buffered = BytesIO()

img = Image.open("/home/giladamar/Desktop/bad_test.jpg")
img.save(buffered, format="JPEG")
img_byte_str = base64.b64encode(buffered.getvalue())
print(len(img_byte_str))

img_str = img_byte_str.decode("utf-8")
print("img_str: ", len(img_str))

img_byte_str = img_str.encode("utf-8")
print("img_byte_str: ", len(img_byte_str))

decoded_byte64 = base64.b64decode(img_byte_str)
print("decoded_byte64: ", len(decoded_byte64))

im = Image.open(BytesIO(decoded_byte64))
im.save("image.png", "PNG")
