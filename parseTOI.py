__author__ = 'ankit'

import unirest
import urllib2
dict={}
categoryDict={}
parseCategoryPage={}
def getFunc():
    # These code snippets use an open-source library.
    response = unirest.get("https://devru-times-of-india.p.mashape.com/feeds/feedurllist.cms?catagory=city",headers={"X-Mashape-Key": "95JFT07SX8mshDfKChZmUMH2y41Kp161Em8jsny9K9MpYQLskS", "Accept": "application/json"})
    dict= response.body
    #categoryDict= dict[u'Item']
    for each in dict['Item']:
        categoryDict[each['name']]=each['defaulturl']
    #print categoryDict['Business']
    for key,value in categoryDict.iteritems():
        responseFromBrowser=urllib2.urlopen(value)
        parseCategoryPage= responseFromBrowser.read()
        print parseCategoryPage


if __name__ == "__main__":
    getFunc()

