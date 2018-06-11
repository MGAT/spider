# coding:utf-8

import urllib
import urllib2

def loadPage(url, filename):
	print "Loading:" + filename
	headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
	request = urllib2.Request(url, headers=headers)
	response = urllib2.urlopen(request)
	return response.read()



def writeFile(html, filename):
	print "Saving:" + filename
	with open (filename, "w") as f:
		f.write(html)
	print "-" * 20


def tiebaSpider(url, beginPage, endPage):
	for page in range(beginPage, endPage+1):
		pn = (page - 1) * 50
		filename = str(page) + ".html"
		fullurl = url + "&pn=" + str(pn)
		print fullurl

		html = loadPage(fullurl, filename)
		writeFile(html, filename)



if __name__ == "__main__":
	kw = raw_input("please enter name:")
	beginPage = int(raw_input("please enter the begin page:"))
	endPage = int(raw_input("please enter the end page:"))
	url = "http://tieba.baidu.com/f?"
	key = urllib.urlencode({"kw": kw})
	url = url + key
	tiebaSpider(url, beginPage, endPage)