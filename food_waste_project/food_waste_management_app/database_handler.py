import cv2
import json
from .models import *
from .scanner import barcodeReader


def list_user_products(username):
    result = UserProduct.objects.filter(User.username == username)
    return result


def get_user_id(username):
    result = User.objects.filter(User.username == username)
    return result.user_id


def scan_barcode():
    cap = cv2.VideoCapture(0)
    while (True):
        ret, frame = cap.read()
        barcode = barcodeReader(frame)
        if barcode is not None:
            print(barcode)
            return barcode
        # if code == ord('q'):
        #     break


def add_user_product(username):
    barcode_info = scan_barcode()
    barcode = barcode_info['barcode']
    #     is in DB?
    try:
        result = Barcode.objects.filter(Barcode.barcode_no == barcode)
        user = User.objects.filter(User.username == username)
        user.barcode_no = barcode
        user.save()
    except:
        result = 'does not exist'

    return result


def new_barcode(new_bar):
    new_bar = Barcode()
    new_bar.barcode_no = new_bar['barcode']
    new_bar.product_name = new_bar['name']
    new_bar.save()
