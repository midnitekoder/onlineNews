import requests
import urllib2
import csv
from bs4 import BeautifulSoup
topicList=[]


def parsingSitemap():

	
	sitemapUrl="https://www.quora.com/sitemap/alphabetical_topics/"
	for i in range(ord('a'), ord('z')+1):
		for j in range(ord('a'), ord('z')+1):
			try:
				tempChar=[]
				tempChar.append(chr(i))
				tempChar.append(chr(j))
				tempChar=''.join(tempChar)
				response=urllib2.urlopen(sitemapUrl+tempChar)
				htmlContent = response.read()
				soup=BeautifulSoup(htmlContent)

				letters=soup.find_all('a')

				for each in letters:
					topicUrl={}
					if each.string[:2].lower()==tempChar:
						topicUrl['Topic']=each.string
						topicUrl['url']=each['href']
						topicList.append(topicUrl)
						#print topicList
						print topicUrl
						"""with open('QuoraTopicUrl.csv', 'wb') as fp:
							w=csv.DictWriter(fp, topicUrl.keys())
    						w.writeheader()
    						w.writerow(topicUrl)"""
			except Exception:
				a=5
	
	for i in range(ord('a'), ord('z')+1):
		try: 
			tempChar=[]
			tempChar.append(chr(i))
			tempChar.append('0')
			tempChar=''.join(tempChar)
			response=urllib2.urlopen(sitemapUrl+tempChar)
			htmlContent=response.read()
			soup=BeautifulSoup(htmlContent)

			letters=soup.find_all('a')

	
			for each in letters:
				topicUrl={}
				if each.string[:2].lower()==tempChar:
					topicUrl['Topic']=each.string
					topicUrl['url']=each['href']
					topicList.append(topicUrl)
					#print topicList
					print topicUrl	
		except Exception:
			a=5

		try:
			tempChar=[]
			tempChar.append(')')
			tempChar.append(chr(i))
			tempChar=''.join(tempChar)
			response=urllib2.urlopen(sitemapUrl+tempChar)
			htmlContent=response.read()
			soup=BeautifulSoup(htmlContent)
		
			letters=soup.find_all('a')

	
			for each in letters:
				topicUrl={}
				if each.string[:2].lower()==tempChar:
					topicUrl['Topic']=each.string
					topicUrl['url']=each['href']
					topicList.append(topicUrl)
					#print topicList
					print topicUrl
		except Exception:
			a=5
		




if __name__ == "__main__":
    parsingSitemap()

