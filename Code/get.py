# -*- coding: utf-8 -*-
import os
import sys
import codecs
import chardet


def get(name, path):
    article = u"""{
"Title": "-.-",
"Model": "algorithm.model"
}
------> DD: Content
# -.-
------> DD: Code
```|||```
"""
    article = article.replace(u'-.-', name)
    article = article.replace(u'|||', path)
    with codecs.open('../Localsite/%s' % (name+'.article'), 'w', 'utf-8') as fout:
        fout.write(article)
    print 'Already get %s from "%s"' % (name, path)


def make(name, path):
    article = u"""{
"Title": "-.-",
"Model": "normal.model"
}
------> DD: Content
|||
"""
    with codecs.open(path, 'r', 'utf-8') as fin:
        article = article.replace(u'|||', fin.read())
    article = article.replace(u'-.-', name)
    with codecs.open('../Localsite/%s' % (name+'.article'), 'w', 'utf-8') as fout:
        fout.write(article)
    print 'Already make %s from "%s"' % (name, path)


def indexList(items):
    article = u''
    for name in items:
        article += u'- [%s](Website/%s.html)\n' % (name, name)
    return article


def main():
    Algorithms = {
            u'01背包': u'../../Algorithms/DP/01背包/code.c',
            u'CLJ树': u'../../Algorithms/树/CLJ.cpp',
            u'并查集': u'../../Algorithms/并查集/code.c',
            u'快速排序': u'../../Algorithms/快速排序/code.cpp',
            u'筛法求素数': u'../../Algorithms/筛法求素数/code.cpp',
            u'Floyd': u'../../Algorithms/Floyd/code.cpp',
            u'KMP': u'../../Algorithms/KMP/code.cpp',
            }
    Mds = {
            u'论考试的心态': u'../Localsite/论考试的心态.md',
            u'论中文作为象形文字的优势': u'../Localsite/论中文作为象形文字的优势.md',
            }
    for name in Algorithms:
        get(name, Algorithms[name])
    for name in Mds:
        make(name, Mds[name])
    with codecs.open('../Localsite/index.articleGet', 'r', 'utf-8') as fin:
        index = fin.read()
    il = indexList(Algorithms)
    ml = indexList(Mds)
    newIndex = index.replace(u'{{Algorithms}}', il)
    newIndex = newIndex.replace(u'{{Mds}}', ml)
    print 'il:'
    print il
    print 'ml:'
    print ml
    print 'newIndex:'
    print newIndex
    with codecs.open('../Localsite/index.article', 'w', 'utf-8') as fout:
        fout.write(newIndex)


if __name__ == '__main__':
    main()
