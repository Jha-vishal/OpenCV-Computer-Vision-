from pyzbar import pyzbar
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        print("detected barcode:", obj)
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    return image

"""decode() function takes an image as a numpy array, and uses pyzbar.decode() that is responsible for decoding 
all barcodes from a single image and returns a bunch of useful information about each barcode detected.
We then iterate over all detected barcodes and draw a rectangle around the barcode and prints the type
and the data of the barcode.
To make things clear, the following is how each obj looked like if we print it:"""

Decoded(data=b'43770929851162', type='I25', rect=Rect(left=62, top=0, width=694, height=180), polygon=[Point(x=62, y=1), Point(x=62, y=179), Point(x=756, y=180), Point(x=756, y=0)])

def draw_barcode(decoded, image):
        n_points = len(decoded.polygon)
        for i in range(n_points):
            image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
            #uncomment above and comment below if you want to draw a polygon and not a rectangle
            #image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
            color=(0, 255, 0), thickness=5)

        return image

if __name__ == "__main__":
    from glob import glob

    barcodes = glob("barcode*.png")
    for barcode_file in barcodes:
        # load the image to opencv
        img = cv2.imread(barcode_file)
        # decode detected barcodes & get the image
        # that is drawn
        img = decode(img)
        # show the image
        cv2.imshow("img", img)
        cv2.waitKey(0)