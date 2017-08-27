import mechanize
from lxml import etree
from bs4 import BeautifulSoup

browser = mechanize.Browser()
response = browser.open("http://quotes.toscrape.com")
print response.info()
page = response.read()
soup = BeautifulSoup(page,"lxml")
print soup.head
print soup.title
for string in soup.strings:
  print(repr(string))
for link in soup.find_all('a'):
  print("%s\n" % link)
