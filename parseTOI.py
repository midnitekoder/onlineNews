__author__ = 'ankit'

import unirest
import urllib2
import json
from dateutil.parser import parse
from datetime import datetime
#parse("Jan 13, 2016, 07.40AM IST")

dict={}
categoryDict={}
parseCategoryPage={}
def getFunc():
    # These code snippets use an open-source library, unirest.
    response = unirest.get("https://devru-times-of-india.p.mashape.com/feeds/feedurllist.cms?catagory=city",headers={"X-Mashape-Key": "95JFT07SX8mshDfKChZmUMH2y41Kp161Em8jsny9K9MpYQLskS", "Accept": "application/json"})
    dict= response.body
    #categoryDict= dict[u'Item']
    for each in dict['Item']:
        categoryDict[each['name']]=each['defaulturl']
    #print categoryDict['Business']
    for key,value in categoryDict.iteritems():
        responseFromBrowser=urllib2.urlopen(value)
        parseCategoryPage=json.loads(responseFromBrowser.read())
        print parseCategoryPage["NewsItem"]
        newsStories={}
        allStories=[]
        for each2 in parseCategoryPage["NewsItem"]:
            newsStories={}
            try:
                print each2['MediaDate']
                if (parse(each2['MediaDate']).date()==datetime.now().date()):
                    print "Inside MediaDate"
                    newsStories['Category']=key
                    newsStories['Headline']=each2["HeadLine"]
                    newsStories['MediaDate']=each2['MediaDate']
                    try:
                        newsStories['NewsPageUrl']=each2["WebUrl"]
                    except Exception:
                        newsStories['NewsPageUrl']=each2["WebURL"]
                    #print newsStories
            except Exception:
                print each2
                print each2['DateLine']
                if (parse(each2['DateLine']).date()==datetime.now().date()):
                    newsStories['Category']=key
                    newsStories['Headline']=each2["HeadLine"]
                    newsStories['MediaDate']=each2['DateLine']
                    try:
                        newsStories['NewsPageUrl']=each2["WebUrl"]
                    except Exception:
                        newsStories['NewsPageUrl']=each2["WebURL"]
            if(newsStories):
                allStories.append(newsStories)
        print allStories
    print "Final all Stories", allStories




if __name__ == "__main__":
    getFunc()

