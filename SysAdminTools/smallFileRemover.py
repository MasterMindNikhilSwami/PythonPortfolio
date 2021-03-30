import os,sys
files = os.listdir()


for file in files:
	try:
		thresholdMB=1
		sizeMB=os.stat("./"+file).st_size/1024/1024
		# print("{1} \t uses= {0:0.2f}".format( sizeMB, file ))
		os.remove(file) if (sizeMB < thresholdMB) and os.path.isfile(file) and file != __file__.split("\\")[-1] else None
	except Exception as e:
		print(e)


# a= list(filter(lambda x:"mp4" or "mkv" in x, files))
# print(a)