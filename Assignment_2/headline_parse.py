from bs4 import BeautifulSoup as bs
import urllib2
import simplejson
import sys
from alchemyapi import AlchemyAPI

#sys.path.append('../../a2/xzvf/Assignment_2/')
#import alchemytest

KEY = 'https://ajax.googleapis.com/ajax/services/search/news?v=1.0&userip=INSERT-USER-IP&q='
VALUE = 'GOOG'

AL_KEY = open('../../api_key.txt','rb').read()[:-1]

def alcObj():
        return AlchemyAPI(AL_KEY)


def sentAn(obj, text):
        response = obj.sentiment("text", text)
        try:
                score    = response[u'docSentiment'][u'score']
        except:
                score    = 0
        type     = response[u'docSentiment'][u'type']
        return score, type

def collect_data():
        url = (KEY + VALUE)

        request = urllib2.Request(url, None)
        response = urllib2.urlopen(request)

        # Process the JSON string.
        results = simplejson.load(response)

        return results

def parsing(data_collected):
        headline_list=[]
        stories = data_collected['responseData']['results']#['titleNoFormatting']
        for story in stories:
                headline_list.append( story['titleNoFormatting'])
        return headline_list

def main():
        obj = alcObj()
        soln = collect_data()
#       print soln
        hlist=parsing(soln)
        for head in hlist:
                score, type = sentAn(obj, head)
                print "\n"+head
                print score , type
main()
