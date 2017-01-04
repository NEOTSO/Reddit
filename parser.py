# -*- coding: utf-8 -*-
import re
import os

class Parser(object):
    
    def parse(self, html):
        pattern = re.compile('<div class=" thing.*?link ".*?class="thumbnail.*?href="(.*?)".*?clearleft', re.S)
        items = re.findall(pattern, html)
        content = [] 
        for item in items:
            with open('src.txt', 'a') as f:
                f.write(item + '\n')
                # content.append(img)

        return content
