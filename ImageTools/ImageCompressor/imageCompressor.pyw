# Credits: NIKHIL SWAMI
# USAGE
# KEEP ALL FILES IN FOLDER ALONG WITH THIS CODE.
# CODE IS SELF EXPLANATORY THOUGH

import os
from PIL import Image
import multiprocessing


WORKING_DIR='C:\\Users\\dell\\Downloads\\Screenshots\\Screenshots'
os.chdir(WORKING_DIR)
if not os.path.exists('compressed'): os.makedirs('compressed')


def custom_resize(sizetupleXY,factor=0.8):
	x,y=sizetupleXY
	x=int(x*factor) 
	y=int(y*factor) 
	# if 
	return (x,y)

def compress_file(imgpath,savings):
	# savings.value+=1
	# for x in imgpathlist:
	x=imgpath
	size=os.path.getsize(x)
	currentImg=Image.open(x).convert('RGB')
	currentImg=currentImg.resize(custom_resize(currentImg.size,factor=1))
	savingName=x.split('.')[0]+'.jpg'
	currentImg=currentImg.save(f'./compressed/{savingName}',quality=85,optimize=False)
	sizeDifference=size - os.path.getsize(f'./compressed/{savingName}')
	savings.value+=sizeDifference
	print('net savings :: ',savings.value/1_000_000,'MB')


def get_images():
	return [x for x in os.listdir() if 'png' in x or 'jpg' in x or 'jpeg' in x or 'webp' in x][:]

if __name__ == '__main__':
	POOL=multiprocessing.Pool(4)
	savings=multiprocessing.Manager().Value('i',0,lock=True)
	result=[POOL.apply_async(compress_file,(file,savings)) for file in get_images()]
	[x.get() for x in result]



	if test:
		# singleThead=[compress_file(x,savings) for x in get_images()]
		...