# -*- coding: utf-8 -*_

import urllib
import os

class Outputer(object):
    
    def output(self, path, items):
        self.mkdir(path)
        for item in items:
            print 'downloading #' + item
            self.save(path, item)

    def mkdir(self, path):
        isExist = os.path.exists(path)
        if not isExist:
            print '######新建文件夹%s' %path
            os.makedirs(path)
        else:
            print '######文件夹%s已存在'
        return

    def save(self, path, src):
        name = src.split('/')[-1]
        try:
            data = urllib.urlopen(src).read()
        except Exception as e:
            print 'error#' + src
        with open(path + '/' + name, 'wb') as f:
            f.write(data)

