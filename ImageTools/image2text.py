from PIL import Image
from PIL import ImageGrab
import os
from pytesseract import image_to_string
# from pdf2image import convert_from_path 

def newest_file(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

# newest_file('')
# the latest image in downloads folder will be converted to text! change dell -> your username for different pc
#my username is dell

def read_image(path):
	o=os.system(f'tesseract "{path}" outfile  --oem 2 pdf ',)


testfile='C:\\Users\\dell\\Downloads\\Screenshot_2021-03-25 KTR ( KTRTRS) Twitter.png'
tempbw=Image.open(testfile).convert('LA').save('tempbw.png')

read_image('tempbw.png')
# text=image_to_string(Image.open(latest))
# print (text)