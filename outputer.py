# -*- coding: utf-8 -*_

import urllib
import os
import re

class Outputer(object):
    def __init__(self):
        self.image = set([])
        self.video = set([])

    def output(self, srcs):
        self.classify(srcs)
        self.saveImage(self.image)
        self.saveVideo(self.video)
        return

    def classify(self, srcs):
        for src in srcs:
            suffix = src.split('/')[-1]
            isImage = re.search(r'\.', suffix)
            if isImage:
                self.image.add(src)
            else:
                self.video.add(src)
        return

    def saveImage(self, srcs):
        with open('image.txt', 'a') as f:
            for src in srcs:
                f.write(src + '\n')
        return

    def saveVideo(self, srcs):
        with open('video.txt', 'a') as f:
            for src in srcs:
                f.write(src + '\n')
        return

    def classifyVideo(self, src):
        return

    def gfycat(self, src):
        return

