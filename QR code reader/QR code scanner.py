import cv2
import numpy as np
from pyzbar.pyzbar import decode
"""
img = cv2.imread('QR.png')     # To Read barcode/QR code image from directory
code = decode(img)
print(code)
                                    # Output = [Decoded(data=b'http://www.scscan.cn', type='QRCODE', rect=Rect(left=86, top=296,
                                    # width=160, height=172), polygon=[Point(x=86, y=296), Point(x=87, y=467), Point(x=246, y=468), Point(x=246, y=297)])]

for barcode in decode(img):
    print(barcode.data)             #Output = b'http://www.scscan.cn'   Initial b' represents bits.


for barcode in decode(img):
    print(barcode.rect)             #Output = Rect(left=86, top=296, width=160, height=172)
    myData = barcode.data.decode('utf-8')
    print(myData)                   #Output = http://www.scscan.cn

"""


""" For web cam access and video capturing """
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 255), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(1)