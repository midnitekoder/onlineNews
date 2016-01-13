__author__ = 'ankit'
#This program extracts date from the Times of India website through a public API and the output is the list of dictionary of each news on the website.
import unirest
import urllib2
import json
from dateutil.parser import parse
from datetime import datetime
#parse("Jan 13, 2016, 07.40AM IST")

dict={}                 #response from the TOI API is saved in it.
categoryDict={}         #key is Category (like sports, business) and value is the url to the data containing all the stories in the category
parseCategoryPage={}    #The string containing all the data about the stories in the category is converted into dictionary. 
allStories=[]           #List of dictionary of all the news on TOI such each dictionary contains headline, mediadate, link to page and category. 
def getFunc():
    # These code snippets use an open-source library, unirest and gets category wise links to the page containing information about the category.
    response = unirest.get("https://devru-times-of-india.p.mashape.com/feeds/feedurllist.cms?catagory=city",headers={"X-Mashape-Key": "95JFT07SX8mshDfKChZmUMH2y41Kp161Em8jsny9K9MpYQLskS", "Accept": "application/json"})
    dict= response.body
    #categoryDict= dict[u'Item']
    for each in dict['Item']:
        categoryDict[each['name']]=each['defaulturl']
    #print categoryDict['Business']
    for key,value in categoryDict.iteritems():
        responseFromBrowser=urllib2.urlopen(value)
        parseCategoryPage=json.loads(responseFromBrowser.read())
        #print parseCategoryPage["NewsItem"]
        for each2 in parseCategoryPage["NewsItem"]:
            newsStory={}          #Dictionary of each individual story. It contains fields MediaDate, Category, Headline, NewsPageUrl.
            try:                   #Some data dictionary uses the word 'MediaDate' while others use 'DateLine'.
                #print each2['MediaDate']
                if (parse(each2['MediaDate']).date()==datetime.now().date()):
                    newsStory['Category']=key
                    newsStory['Headline']=each2["HeadLine"]
                    newsStory['MediaDate']=each2['MediaDate']
                    try:            #Some data dictionary uses the word 'WebUrl' while others use 'WebURL'
                        newsStory['NewsPageUrl']=each2["WebUrl"]
                    except Exception:
                        newsStory['NewsPageUrl']=each2["WebURL"]
                    #print newsStory
            except Exception:
                try:              #Some categories like Photos and Videos don't have MediaDate associated with them. They are given the present date.
                    #print each2
                    #print each2['DateLine']
                    if (parse(each2['DateLine']).date()==datetime.now().date()):
                        newsStory['Category']=key
                        newsStory['Headline']=each2["HeadLine"]
                        newsStory['MediaDate']=each2['DateLine']
                        try:
                            newsStory['NewsPageUrl']=each2["WebUrl"]
                        except Exception:
                            newsStory['NewsPageUrl']=each2["WebURL"]
                except Exception:
                    newsStory['MediaDate']=datetime.now().date()
                    newsStory['Category']=key
                    newsStory['Headline']=each2["HeadLine"]
                    try:
                            newsStory['NewsPageUrl']=each2["WebUrl"]
                    except Exception:
                            newsStory['NewsPageUrl']=each2["WebURL"]

            if(newsStory):
                allStories.append(newsStory)
    print "Final all Stories", allStories
    print "Successfully extracted data!"



if __name__ == "__main__":
    getFunc()

