import modulex as mx
import hashlib
import requests
import os
from PIL import Image



# ------------------------------------
def data_splitter(dataList,pieces):
	dataparts2D=[]
	for d in range(pieces):
		step=int(len(dataList)/pieces)+1
		subdata=dataList[d*step:(d+1)*step]
		dataparts2D.append(subdata)
	return dataparts2D

def write_multi_thread(workfn,work,parallelism=4,waitfinish=0):
	import threading

	work2D=data_splitter(work,4)
	threadpool=[threading.Thread(target=workfn,args=(work2D[x],)) for x in range(parallelism)]
	[x.start() for x in threadpool]
	if not waitfinish:
		[x.join() for x in threadpool]
	print('trace1')
	return threadpool

# ------------------------------------
def write_images(urllist,dirname='./images/'):
	mx.touch(dirname+'init.txt')
	for x in urllist:
		filename=hashlib.md5(x.encode()).hexdigest()
		filepath=f'./{dirname}{filename}'
		print('writing',filepath)
		if not os.path.exists(filepath):
			print('downloading=>',x)
			data=requests.get(x).content
			try:
				open(filepath,'wb').write(data)
				iformat=Image.open(filepath).format
				os.rename(filepath,f'{filepath}.{iformat}')
				print('writing=>',x,filepath)
			except Exception as e:
				print('failed',x,'because',e)

# ------------------------------------
def select_images_from_page(url,selector,trimparams='true'):
	images=set()
	for x in mx.get_page_soup(url).select(selector):

		for attrval in x.attrs.values():
			if 'http' in attrval:
				if trimparams:
					attrval=attrval.split('?')[0]
				images.add(attrval)
	return list(images)

def get_urls_from_json(ajaxurl):
	jobject=mx.jloads(mx.get_page(ajaxurl).text)
	urls=[x['data']['media']['src'].split('?')[0] for x in jobject]
	return urls
# ------------------------------------
url='https://yandex.com/images/search?text=nature'
def yandex_macro():
	def yandex_image_gatherer(markup):#OFFLINE MODE FROM FILE MARKUP
		resultPageSoup=mx.make_soup(markup)
		results=resultPageSoup.select('.serp-item[data-bem]')
		urls=[mx.jloads(x['data-bem'])['serp-item']['img_href'] for x in results]
		return urls
	markup=mx.fread('./rawData/yashresults1.html')
	bigWorkList=yandex_image_gatherer(markup)
	threadpool=write_multi_thread(write_images,bigWorkList)
	[x.start() for x in threadpool];
	[x.join() for x in threadpool];

# ------------------------------------
if __name__ == '__main__':
	url='https://www.goodhousekeeping.com/life/g22521771/happy-quotes/'
	ajaxurl='https://www.goodhousekeeping.com/ajax/contentmedia/?id=2988fa18-71f9-432f-a608-281221ae15f9'
	selector='picture source'
	imagelist=select_images_from_page(url,selector)
	# imagelist=get_urls_from_json(ajaxurl)
	write_multi_thread(write_images,imagelist)
	# print(imagelist,len(imagelist))

