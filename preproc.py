import cv2
from PIL import Image
import numpy as np
import pytesseract

names = cv2.imread('names.png',0)
chat = cv2.imread('chat.png',0)

current = names

ret, thresh = cv2.threshold(current, 127, 255, cv2.THRESH_BINARY)
thresh = cv2.bitwise_not(thresh)

cv2.imshow('image',thresh)
print(pytesseract.image_to_string(thresh).strip().split("\n"))
#print("--------\n")
#print(pytesseract.image_to_string(chat).strip())

cv2.waitKey(0)
cv2.destroyAllWindows()