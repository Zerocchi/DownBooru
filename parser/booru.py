__author__ = 'zerocchi'

from bs4 import BeautifulSoup
import urllib.request


class Booru:

    @staticmethod
    def get_data(url):
        """
        :param url: pass full url to get the JSON/XML raw data
        :return: JSON/XML raw data
        """
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response)
        return soup

    def parse(self):
        """
        parse() method return a list consists of images URL.
        :return: list of images URL.
        """
        raise NotImplementedError("parse() method not implemented.")


class Gelbooru(Booru):

    base_url = "http://gelbooru.com"

    def __init__(self, tags, limit):
        self.url = self.base_url + u"/index.php?page=dapi" \
                                   u"&s=post&q=index&tags={0}&limit={1}".format(tags, limit)

    def parse(self):
        data = super().get_data(self.url)
        links = [dict(post.attrs)['file_url'] for post in data.findAll('post')]
        return links


class Danbooru(Booru):

    base_url = "https://danbooru.donmai.us"

    def __init__(self, tags, limit):
        tags = tags.split()
        self.url = self.base_url + "/posts.xml?tags=%s&limit=%s" % ("+".join(tags), limit)

    def parse(self):
        data = super().get_data(self.url)
        links = [self.base_url + post.find('file-url').string.strip() for
                 post in data.findAll('post') if post is not None]
        return links


class Safebooru(Gelbooru):

    base_url = "http://safebooru.org"

    def __init__(self, limit, tags):
        super().__init__(limit, tags)


class Rule34(Gelbooru):

    base_url = "http://rule34.xxx"

    def __init__(self, tags, limit):
        super().__init__(tags, limit)
