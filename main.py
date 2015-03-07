__author__ = 'zerocchi'

from parser.booru import Gelbooru, Danbooru, Safebooru, Konachan, Rule34, Yandere
import datetime as dt
import os
import urllib.request


def runbooru(tags, limit=0, booru="Danbooru"):
    tag = Danbooru(tags, limit)
    if booru == "danbooru":
        tag = Danbooru(tags, limit)
    elif booru == "gelbooru":
        tag = Gelbooru(tags, limit)
    elif booru == "rule34":
        tag = Rule34(tags, limit)
    elif booru == "konachan":
        tag = Konachan(tags, limit)
    elif booru == "yandere":
        tag = Yandere(tags, limit)
    elif booru == "safebooru":
        tag = Safebooru(tags, limit)
    return tag


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
    tag = str(input("Enter tags: "))
    limit = input("Enter limit: ")
    booru = str(input("Enter booru: "))
    tag = runbooru(tag, limit, booru.lower())
    makefile("/home/user/Images")
    [urllib.request.urlretrieve(url, "{0}/{1}".format(os.getcwd(), url.split("/")[-1])) for url in tag.parse()]
