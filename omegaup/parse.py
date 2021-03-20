from html.parser import HTMLParser
from urllib.request import urlopen

class OmegaupProblemParse(HTMLParser):
	'''
	fix this shit maybe later :D!!
	def __init__(self, folder):
		HTMLParser.__init__(self)
	'''
	def handle_starttag(self, tag, attrs):
		print("Encountered a start tag:", tag)

	def handle_endtag(self, tag):
		print("Encountered an end tag :", tag)

	def handle_data(self, data):
		return data
		print("Encountered some data  :", data)

test = OmegaupProblemParse()
file = input()
html = urlopen(file).read()
test.feed(html.decode('utf-8'))

algo = test.handle_data(html.decode("utf-8"))

some = algo.split()
print( *some )
print(type(algo))
