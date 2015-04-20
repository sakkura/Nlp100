import json
# -*- coding: utf-8 -*-


article = {}
with open("jawiki-country.json") as fh:
	for line in fh.readlines():
		js = json.loads(line, "utf-8")
		article[js["title"]] = js["text"]
print(article[u"イギリス"])

