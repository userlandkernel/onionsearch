import os
import sys
import bs4
import json
import urllib.parse
from requests_tor import RequestsTor



class TorSearch:
	def __init__(self):
		self.rt = RequestsTor(tor_ports=(9050,), tor_cport=9051)
		engineFile = open('searchengines.json')
		engines = json.load(engineFile)
		self.engines = engines


	def Search(self, q=""):
		qEnc = urllib.parse.quote(q)
		urls = [engine + qEnc for engine in self.engines['get']]
		linkDir = []
		for url in urls:
			try:
				print("GET {}".format(url))
				request = self.rt.get(url)
				result = bs4.BeautifulSoup(request.text, "html.parser")
				links = []
				links = result.find_all("a")
				linkDir.extend(links)
			except Exception as exc:
				continue
		return linkDir

if __name__ == "__main__":
	ts = TorSearch()
	for link in ts.Search("Search Engine"):
		print(link.text, link['href'])