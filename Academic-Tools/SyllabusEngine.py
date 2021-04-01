import requests
import html5lib 
from bs4 import BeautifulSoup as soup
#last Edit 29-03-2021



def generate_syllabus_index(url,separator=','):
	outfilename=url.split('/')[-1]+'.html' if 'html' in url else url.split('/')[-1]
	data=requests.get(url).text
	pagesoup=soup(data,'html.parser') # print(dir(pagesoup))
	maincontent=pagesoup
	br=pagesoup.new_tag('br')
	for p in maincontent.select('p'):
		p.append(br)
		try:
			keywords=p.text.split(',')
			# print('TRACE111')
			print(keywords)
			# p.string=''
			anchors=[pagesoup.new_tag('a',href=f'https://www.google.com/search?&q={kw}') for kw in keywords]

			for a,kw in zip(anchors,keywords):
				a.string=kw
				# p.append(a)
		except :
			...
			# [a.append(br) for a in p.select('a')]

			# p.string=''
			# p.append(x for x in reparsed)
			# print(soup.new_tag(p,'a',href='.com'))

		# print(p.contents)
	open(outfilename+'.html','w').write(str(maincontent))
url='http://www.jnu.ac.in/se-cse-syllabus'

for x in range(5):
	generate_syllabus_index(url)