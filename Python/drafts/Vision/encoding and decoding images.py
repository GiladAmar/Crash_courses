import base64
from io import BytesIO

import numpy as np
from PIL import Image

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


# To instead make sure it is being compressed with jpeg first:
def img_to_base64_str(self, img):
    buffered = BytesIO()
    img.save(buffered, format="jpeg")
    buffered.seek(0)
    img_byte = buffered.getvalue()
    return base64.b64encode(img_byte).decode()

