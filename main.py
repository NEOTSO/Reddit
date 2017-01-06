# -*- coding: utf-8 -*-

import downloader
import parser
import outputer
import random
import time

class Reddit(object):

    def __init__(self):
        self.url = ''
        self.page = 0    #page number you have crawled
        self.downloader = downloader.Downloader()
        self.parser = parser.Parser()
        self.outputer = outputer.Outputer()

    def crawl(self):
        if self.url == '':
            self.url = 'https://www.reddit.com/r/ass/'
        time.sleep(random.randint(1,3))
        html = self.downloader.download(self.url)
        if html == None:
            self.crawl()
        self.page = self.page + 1
        print 'crawling page#' + str(self.page) + '\n' + self.url
        srcs, self.url = self.parser.parse(html)    #return images and videos url
        self.outputer.output(srcs)
        if self.url == None:    #if we can't get nextPage url, crawl ends
            print 'crawling finished\nget ' + str(self.page) + ' pages'
            return
        self.crawl()
        return

if __name__ == '__main__':
    spider = Reddit()
    spider.downloader.over18()
    spider.crawl()
