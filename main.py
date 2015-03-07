__author__ = 'zerocchi'

from parser.booru import Gelbooru, Danbooru, Safebooru, Konachan, Rule34, Yandere
import datetime as dt
import getpass
import os
import sys
import urllib.request


def runbooru(tags, limit=0, booru="Danbooru"):
    processors = {f.__name__: f for f in (Danbooru, Gelbooru, Konachan, Yandere, Safebooru)}
    if booru in processors:
        tag = processors.get(booru, Danbooru)(tags, limit)
    return tag

def dochelp():
    """It should be like this: python main.py <tags> <limit> <booru> with tags enclosed in quotation mark\
 for more than one tag"""

def makefile(path=None):

    if path is not None:
        location = os.path.realpath(path)
    else:
        location = "{}".format(dt.datetime.now().strftime('%Y%m%d%H%M%S'))

    if not os.path.exists(location):
        os.makedirs(location)

    os.chdir(location)
    print(os.path.join(os.path.dirname(__file__)))

if __name__ == "__main__":
    try:
        script, tag, limit, booru = sys.argv
        tag = runbooru(tag, limit, booru)
        makefile("/home/%s/Images" % getpass.getuser())
        [urllib.request.urlretrieve(url, "{0}/{1}".format(os.getcwd(), url.split("/")[-1])) for url in tag.parse()]
    except ValueError:
        print(dochelp.__doc__)
