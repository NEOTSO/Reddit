# -*- coding: utf-8 -*-

import downloader
import parser
import outputer

class Reddit(object):

    def __init__(self):
        self.url = 'https://www.reddit.com/r/ass/?count='
        self.page = 0
        self.downloader = downloader.Downloader()
        self.parser = parser.Parser()
        # self.outputer = outputer.Outputer()

    def crawl(self):
        page = self.page
        url = self.url + str(self.page)
        print 'Mission Begin #' + url
        html = self.downloader.download(url)
        srcs = self.parser.parse(html)
        # self.outputer.output(str(page), srcs)
        print 'Mission Completed'
        return

if __name__ == '__main__':
    spider = Reddit()
    spider.crawl()
