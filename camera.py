import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    #시간 저장
    now = datetime.datetime.now()
    nowDatetime_path = now.strftime('%Y-%m-%d %H_%M_%S')

    ret, frame = capture.read()
    cv2.imshow('test', frame)
    key = cv2.waitKey(30)
    if key == ord('c'):
        cv2.imwrite("capture " + nowDatetime_path + ".jpg", frame)
    elif key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
