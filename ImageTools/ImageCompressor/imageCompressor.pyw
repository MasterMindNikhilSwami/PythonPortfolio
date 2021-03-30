# Credits: NIKHIL SWAMI
# USAGE
# KEEP ALL FILES IN FOLDER ALONG WITH THIS CODE.
# CODE IS SELF EXPLANATORY THOUGH

import os
from PIL import Image

if not os.path.exists('compressed'): os.makedirs('compressed')

def resize1200(currentsize):
	# preserves aspect ratio
	x,y= currentsize
	if x>1200:
		y= int(y*(1200/x))
		x=1200
	return x,y

def const_crop(sizetupleXY,factor=0.8):
	x,y=sizetupleXY
	x=int(x*factor) 
	y=int(y*factor) 
	# if 
	return (x,y)

# print(const_crop((100,200),0.8))

JPG_PNG_LIST=[x for x in os.listdir() if 'png' in x or 'jpg' in x or 'jpeg' in x or 'webp' in x]
for x in JPG_PNG_LIST:
	currentImg=Image.open(x).convert('RGB')
	currentImg=currentImg.resize(const_crop(currentImg.size,factor=0.6),Image.ANTIALIAS)
	currentImg=currentImg.save('./compressed/'+x,quality=75,optimize=True)
print("these files were compressed",JPG_PNG_LIST)

