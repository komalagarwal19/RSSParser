from urllib2 import urlopen
from xml.sax import make_parser, ContentHandler
import sys

"""
This implementation is based on lecture CS107 - Programming Paradigms lecture  
https://see.stanford.edu/Course/CS107/215
Lecture 26 - XML Processing and Python - Two Different XML Processing Models
"""

class RSSContentHandler(ContentHandler):

  def __init__(self):
      ContentHandler.__init__(self)
      self.in_item = False
      self.in_title = False


  def characters(self,data):
      if self.in_title:
          sys.stdout.write(data)
       
  def startElement(self, tag, attrs):
      if tag == "item":
          self.in_item = True
      if tag == "title" and self.in_item:
          self.in_title = True

  def endElement(self, tag):
      if tag == "title" and self.in_title:
          sys.stdout.write("\n")
          self.in_title = False
      if tag == "item":
          self.in_item = False

def extractFeedTitle(url):
  infile = urlopen(url)
  parser = make_parser()
  parser.setContentHandler(RSSContentHandler())
  parser.parse(infile)

extractFeedTitle("http://feeds.bbci.co.uk/news/rss.xml")