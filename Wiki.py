#Written by Jake Schultz
#TODO Add more lang support, limit number of results returned
import re
from urllib2 import Request, urlopen, URLError
import json

WORDS = ["WIKI", "WICKY","ARTICLE"]

PRIORITY = 1


def handle(text, mic, profile):
    # method to get the wiki summary
    get_wiki(text,mic)


def get_wiki(text,mic):
    mic.say("What would you like to learn about?")
    # get the user voice input as string
    article_title = mic.activeListen()
    # make a call to the Wikipedia API
    request = Request('https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles='+article_title)
    try:
        response = urlopen(request)
        data = json.load(response)
        # Parse the JSON to just get the extract. Always get the first summary.
        output = data["query"]["pages"]
        final = output[output.keys()[0]]["extract"]
        mic.say(final)
    except URLError, e:
        mic.say("Unable to reach dictionary API.")


def isValid(text):
    wiki= bool(re.search(r'\Wiki\b',text, re.IGNORECASE))
    # Add 'Wicky' because the STT engine recognizes it quite often
    wicky= bool(re.search(r'\wicky\b',text, re.IGNORECASE))
    article= bool(re.search(r'\article\b',text, re.IGNORECASE))

    if wicky or wiki or article:
        return True
    else:
        return False

