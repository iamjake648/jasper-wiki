#Written by Jake Schultz
#TODO Add more lang support, limit number of results returned
import re
from urllib2 import Request, urlopen, URLError
import json
from pprint import pprint

def get_wiki(article_title):
    #make a call to the API
    request = Request('https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles='+article_title)
    try:
        response = urlopen(request)
        data = json.load(response)
        #Parse the JSON to just get the extract. Always get the first summary.
        output = data["query"]["pages"]
        final = output[output.keys()[0]]["extract"]
        pprint(final)
    except URLError, e:
        print e

get_wiki('Apple')