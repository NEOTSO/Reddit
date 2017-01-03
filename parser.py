# -*- coding: utf-8 -*-
import re
import os

class Parser(object):
    
    def parse(self, html):
        pattern = re.compile('<div class=" thing.*?link ".*?listing" >(.*?)clearleft', re.S)
        items = re.findall(pattern, html)
        content = [] 
        for item in items:
            pattern_2 = re.compile('class="thumbnail.*?href="(.*?)"')
            img = re.findall(pattern_2, item)[0]
            suffix = img.split('/')[-1]
            result = re.search(r'\.', suffix)
            # result = re.search(r'.(jpg|png|gif|gifv|webm)', suffix)
            if result:
                with open('src.txt', 'w') as f:
                    f.write(img + '\n')
                    content.append(img)

        return content
