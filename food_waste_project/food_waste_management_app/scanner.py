from pyzbar.pyzbar import decode
import cv2
import numpy as np


def barcodeReader(image):
    bgr = (8, 70, 208)

    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = decode(gray_img)

    for decodedObject in barcodes:
        points = decodedObject.polygon

        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

    for bc in barcodes:
        cv2.putText(image, bc.data.decode("utf-8") + " - " + bc.type, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    bgr, 2)

        # return "Barcode: {} - Type: {}".format(bc.data.decode("utf-8"), bc.type)
        return {'barcode': bc.data.decode(), 'type': bc.type}


# cap = cv2.VideoCapture(0)
# while (True):
#     ret, frame = cap.read()
#     barcode = barcodeReader(frame)
#     if barcode is not None:
#         print(barcode)
#         break
#     cv2.imshow('Barcode reader', frame)
#     code = cv2.waitKey(10)
#     # if code == ord('q'):
#     #     break
