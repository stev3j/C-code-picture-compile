#pytesseract와 opencv를 같이 이용한 버전

import cv2 as cv
from matplotlib.pyplot import box
import pytesseract as pt
from distutils.ccompiler import new_compiler
import os
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv.imread('test4.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

### start
text = pt.image_to_string(img)

file = open('main.c', 'w', encoding='UTF-8')
file.write(text)
file.close()

compiler = new_compiler()
compiler.compile(['main.c']) #여기서 에러가 뜨면 인식이 잘 못된 것
compiler.link_executable(['main.obj'], 'main')
os.system('main.exe')


### test
hImg, wImg,_ = img.shape
boxes = pt.image_to_boxes(img)
for b in boxes.splitlines():
    # print(b)
    b = b.split(' ')
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv.rectangle(img, (x,hImg-y), (w,hImg-h), (0,0,255), 2)
    cv.putText(img,b[0],(x,hImg-y),cv.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
cv.imshow('Result',img)
cv.waitKey(0)
