# -*- coding: utf-8 -*-
"""将我自定义的article格式转换到html格式。
"""


import os
import sys
import time
import markdown
import json
import codecs


Path = {"Root": "..",
        "Resources": "../Resources",
        "Localsite": "../Localsite",
        "Website": "../Website"
        }


def convert_markdown(content):
    """把一段markdown转换成html
    """
    with codecs.open('tmp.md', 'w') as fout:
        fout.write(content)
    os.system('python -m markdown -x markdown.extensions.tables tmp.md > tmp.html')
    with codecs.open('tmp.html', 'r', 'utf-8') as fin:
        html = fin.read()
    os.remove('tmp.md')
    os.remove('tmp.html')
    return html

def convert(article, outputPath = Path["Website"]):
    """把一篇文章转换成网页。

    默认文章路径已存在。

    参数：
        article: 文章的名字，形如："index" or "Algorithm/qsort"。
    """
    print 'convert article: %s' % article
    path, name = os.path.split(article) # 形如："", "index" or "Algorithm", "qsort"
    with open(os.path.join(os.path.join(Path["Localsite"], 'Articles'), article + '.article'), 'r') as fin:
        allContent = fin.read()
        everyContent = allContent.split('------> DD: ')
    settings = json.loads(everyContent[0])
    # print settings
    for oneContent in everyContent[1:]:
        name, content = oneContent.split('\n', 1)
        # print "->", name, content
        settings[name] = content
        # print settings
    with open(os.path.join(Path["Resources"], settings["Model"]), 'r') as fin:
        model = fin.read()
        html = model
    for name in settings:
        if name != u"Model":
            if name == u"Content":
                new = convert_markdown(settings[name])
                # print "Type:::", type(new)
                sys.stdout.flush()
                html = html.replace(u'{{%s}}' % name, new)
            else:
                html = html.replace(u'{{%s}}' % name, settings[name])
    with codecs.open(os.path.join(outputPath, article + '.html'), 'w', 'utf-8') as fout:
        fout.write(html)


if __name__ == '__main__':
    pass
