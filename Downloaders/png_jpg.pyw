from PIL import Image
import os
[Image.open(x).save(x.replace('.png','.jpg')) for x in os.listdir() if x.endswith('png')]
	
