import html5lib,requests,time,threading,selenium
from selenium import webdriver
from bs4 import BeautifulSoup as soup

def hire_employer_to_download_list(workfn,workdata,employee_count):
	workbench=[]
	workslots=[workdata[i:i + employee_count] for i in range(0, len(workdata), employee_count)]
	idx=0
	nameStringBinderList=[n.split('/')[-1] for n in LINKS]

	for slot in workslots:
		for j in slot:
			try:
				workbench.append( threading.Thread( target=workfn, args=(j,nameStringBinderList[idx]) ) )
				workbench[idx].start()
				# workbench[idx].join()
				idx+=1
			except:
				print('error occured')
		time.sleep(0.5)

def songDownload(url,name):
	reqdata = requests.get(url).content
	with open(str(name)+'.mp3', 'wb') as handler:
	    handler.write(reqdata)
	print('downloaded :'+url)

def write_this(fname,content):
	f=open(fname,"+ab")
	f.write(content)

def open_page(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	fullText=requests.get(url,headers=headers).text
	return fullText

def open_page_with_selenium(url):
	wd.get(url)
	page= wd.page_source
	return page


#SETTING OPTIONS
opts=webdriver.firefox.options.Options()
# opts.headless = True #works standalone
opts.add_argument("--headless") #works standalone
wd = webdriver.Firefox(options=opts)


#START SCRAPING
URL='https://zeldauniverse.net/media/music/majoras-mask-original-soundtrack/'
pagecontent=open_page_with_selenium(URL)
bsoup=soup(pagecontent,features="html5lib")
hyperlinks=bsoup.find_all('a')


#START EXTRACTION OF LINKS
LINKS=[]
for x in hyperlinks:
	try:	
		if '.mp3' in x.get('href'):
			LINKS.append(x.get('href'))
			print(x.get('href'))
	except :
		print('some error')

hire_employer_to_download_list(songDownload,LINKS,5)
# hire_employer(imgDownload,urlWheel,4)
wd.close()

