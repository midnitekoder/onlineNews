__author__ = 'ankit'

import json
import urllib2

def questionTopicFinder():
	topic='BEAN'
	#f=open('quoraTopicsList','r')
	#dataString= f.read()
	for line in open('quoraTopicsList','r'):
		print line
		response=json.loads(line)
		print response
		"""if response['Topic']==topic:
			searchUrl=each['url']
			break
	print searchUrl
	topicPageResponse=urllib2.urlopen(searchUrl)
"""


if __name__ == "__main__":
    questionTopicFinder()
