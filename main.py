__author__ = 'zerocchi'

from parser.booru import Gelbooru, Danbooru, Safebooru, Rule34
import datetime as dt
import os
import urllib.request


def runbooru(tags, limit, booru="Danbooru"):
    tag = Danbooru(tags, limit)
    if booru == "Danbooru":
        tag = Danbooru(tags, limit)
    elif booru == "Gelbooru":
        tag = Gelbooru(tags, limit)
    elif booru == "Rule34":
        tag = Rule34(tags, limit)
    return tag


def makefile(path=None):
    if path is not None:
        location = os.path.realpath(path)
    else:
        location = "{}".format(dt.datetime.now().strftime('%Y%m%d%H%M%S'))

    if not FileExistsError:
        os.mkdir(location)
    os.chdir(location)

if __name__ == "__main__":
    tag = runbooru("aisaka_taiga sex", 6)
    makefile("../Images")
    [urllib.request.urlretrieve(url, "{0}/{1}".format(os.getcwd(), url.split("/")[-1])) for url in tag.parse()]
