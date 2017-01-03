# -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib

class Downloader(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2950.4 Safari/537.36'}
        self.data = {
            'over18': 'yes'
        }
        self.opener = None

    def over18(self):
        url = 'https://www.reddit.com/over18'
        cookieJar = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
        post_data = urllib.urlencode(self.data)
        request = urllib2.Request(url, post_data, self.headers)
        response = self.opener.open(request)

    def download(self, url):
        if url is None:
            return None

        self.over18()

        response = self.opener.open(url)
        if response.getcode() != 200:
            return None
        return response.read()
