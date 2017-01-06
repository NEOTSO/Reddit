# -*- coding: utf-8 -*-
import re
import os

class Parser(object):
    
    def parse(self, html):
        pattern = re.compile('<div class=" thing.*?link ".*?class="thumbnail.*?href="(.*?)".*?clearleft', re.S)
        pattern2 = re.compile('<span class="next-button"><a href="(.*?)" rel="nofollow next" >')
        items = re.findall(pattern, html)
        if re.findall(pattern2, html):
            nextPage = re.findall(pattern2, html)[0]    #nextPage url
        else:
            nextPage = None
        srcs = set([])    #use python set type to avoid duplicate url
        for item in items:
            srcs.add(item)
        return srcs, nextPage
