__author__ = 'ankit'

import unirest

def getFunc():
    # These code snippets use an open-source library.
    response = unirest.get("https://devru-times-of-india.p.mashape.com/feeds/feedurllist.cms?catagory=city",headers={"X-Mashape-Key": "95JFT07SX8mshDfKChZmUMH2y41Kp161Em8jsny9K9MpYQLskS", "Accept": "application/json"})
    print response.body



if __name__ == "__main__":
    getFunc()

