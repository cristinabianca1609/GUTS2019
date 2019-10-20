from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO
import base64

def decode_b64_img(data):
    im = Image.open(BytesIO(base64.b64decode(data)))
    code = decode(im)
    return code
