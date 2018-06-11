import requests
import json
from lxml import etree

page = 1
url = "http://www.qiushibaike.com/8hr/page/" + str(page)
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

response = requests.get(url, headers=headers)
resHtml = response.text

html = etree.HTML(resHtml)

result = html.xpath('//div[contains(@id, "qiushi_tag")]')

items = []
for site in result:
	item = {}

	image = site.xpath('.//div[@class="thumb"]//@src')
	print  image
	username = site.xpath("./div//h2")[0].text
	print username
	content = site.xpath('.//div[@class="content"]/span')[0].text.strip()
	print content
	vote = site.xpath('.//i')[0].text
	print vote
	comments = site.xpath('.//i')[1].text
	print comments

	item["username"] = username
	item["image"] = image
	item["content"] = content,
	item["comments"] = comments
	item["vote"] = vote

	items.append(item)

with open("qiushi.json", "a") as f:
	f.write(json.dumps(items, ensure_ascii=False).encode("utf-8") + "\n")




