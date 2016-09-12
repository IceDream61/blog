# -*- coding: utf-8 -*-
"""一键生成IceWorld网站的工具。
"""


import os
import sys
import time
from convert import convert


# 或许没啥用
Path = {"Root": "..",
        "Resources": "../Resources",
        "Localsite": "../Localsite",
        "Website": "../Website"
        }


def makeIndex():
    """生成站点主页。
    """
    convert('index', Path["Root"])


def makeNormal():
    """生成普通文章。
    """
    if not os.path.exists('../Website'):
        os.mkdir('../Website')
    articles = []
    for article in os.listdir(os.path.join(Path["Localsite"], 'Articles')):
        if article.startswith('.'):
            continue
        name, ext = os.path.splitext(article) # 形如："联系我们", ".article"
        if ext == '.article':
            articles.append(name)
    if 'index' in articles:
        articles.remove('index')
    print 'get articles: %s' % articles # 形如：["index", "联系我们"]
    for article in articles:
        convert(article)


def makeAlgorithm():
    """生成算法文章。
    """
    if not os.path.exists('../Website'):
        os.mkdir('../Website')
    if not os.path.exists('../Website/Algorithm'):
        os.mkdir('../Website/Algorithm')
    articles = []
    for article in os.listdir(os.path.join(Path["Localsite"], 'Algorithm')):
        if article.startswith('.'):
            continue
        name, ext = os.path.splitext(article)
        if ext == '.article':
            articles.append(name)
    for article in articles:
        convert(article)


def make():
    """生成整个网站
    """
    makeIndex()
    makeNormal()
#   makeAlgorithm()


if __name__ == '__main__':
    make()
