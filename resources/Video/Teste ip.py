import cv2
import urllib.request
import numpy as np


cap = cv2.VideoCapture(1)
url = 'http://192.168.0.106:8080/video.jpg'
imgResp = urllib.request.urlopen('http://192.168.0.106:8080/video.')

imgNP = np.array(bytearray(imgResp.read()), dtype=np.uint8)
imge = cv2.imdecode(imgNP, -1)
cv2.imshow('testa  ', imge)
cv2.waitKey(0)
