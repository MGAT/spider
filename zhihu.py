from bs4 import BeautifulSoup
import requests
import time

def captcha(captcha_data):
	with open("captcha.jpg", "wb") as f:
		f.write(captcha_data)
	text = raw_input("please write the captcha: ")
	return text

def zhihuLogin():
	sess = requests.Session()
	headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

	html = sess.get("https://www.zhihu.com/#singin", headers=headers).text
	bs = BeautifulSoup(html, 'lxml')

	_xsrf = bs.find("input", attrs={"name": "_xsrf"}).get("value")
	captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time() * 1000) 

	captcha_data = sess.get(captcha_url, headers=headers)

	text = captcha(captcha_data)

	data = {
		"_xsrf": _xsrf,
		"email": "1______5",
		"password": "c_____c",
		"captcha": text
	}

	response = sess.post("https://www.zhihu.com/login/email", data=data, headers=headers)

	response = sess.get("https://www.com/people/chenxucai/activities", headers=headers)

	with open("my.html", "w") as f:
		f.write(response.text.encode("utf-8"))

if __name__ == "__main__":
	zhihuLogin()