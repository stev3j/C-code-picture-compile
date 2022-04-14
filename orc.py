#pytesseract만 이용한 버전
from PIL import Image
import pytesseract as pt
from distutils.ccompiler import new_compiler
import os
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open('test1.jpg')

text = pt.image_to_string(img)
text = '#include <stdio.h>\nint main(){\nprintf("Hi");\nreturn 0;\n}'

file = open('main.c', 'w')
file.write(text)
file.close()

compiler = new_compiler()
compiler.compile(['main.c'])
compiler.link_executable(['main.obj'], 'main')
os.system('main.exe')

#print(text)
