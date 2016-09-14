# -*- coding: utf-8 -*-
"""将我自定义的article格式转换到html格式。
"""


import os
import sys
import time
import markdown
import json
import codecs


DebugCount = 0
Path = {"Root": "..",
        "Resources": "../Resources",
        "Localsite": "../Localsite",
        "Website": "../Website"
        }


def Debug(string):
    global DebugCount
    DebugCount += 1
    print 'string %d type %s' % (DebugCount, type(string))


def alterFiles(content):
    """把article里面包含的文件都引入进来。

    article中引入文件的格式是：```<filename>```
    """
    while True:
        i = content.find('```')
        if i == -1:
            break
        j = i+3 + content[i+3:].find('```')
        with codecs.open(content[i+3:j], 'r', 'utf-8') as fin:
            t = fin.read()
            # Debug(t)
            content = content[:i] + t + content[j+3:]
    return content


def cpp_html(content):
    """把一段cpp转换成html
    """
    html = content
    html = html.replace(u'&', u'&#38;')
    html = html.replace(u' ', u'&#160;')
    html = html.replace(u'<', u'&#60;')
    html = html.replace(u'>', u'&#62;')
    html = html.replace(u'"', u'&#34;')
    html = html.replace(u"'", u'&#39;')
    return html


def markdown_html(content):
    """把一段markdown转换成html
    """
    with codecs.open('tmp.md', 'w', 'utf-8') as fout:
        # Debug(content)
        fout.write(content)
    os.system('python -m markdown -x markdown.extensions.tables tmp.md > tmp.html')
    with codecs.open('tmp.html', 'r', 'utf-8') as fin:
        t = fin.read()
        # Debug(t)
        html = t
    os.remove('tmp.md')
    os.remove('tmp.html')
    return html


def article_html(article, outputPath = Path["Website"]):
    """把一篇文章转换成网页。

    默认文章路径已存在。

    参数：
        article: 文章的名字，形如："index" or "Algorithm/qsort"。
    """
    print 'article_html article: %s' % article
    path, name = os.path.split(article) # 形如："", "index" or "Algorithm", "qsort"
    with codecs.open(os.path.join(Path["Localsite"], article + '.article'), 'r', 'utf-8') as fin:
        allContent = fin.read()
        allContent = alterFiles(allContent)
        # Debug(allContent)
        everyContent = allContent.split('------> DD: ')
    settings = json.loads(everyContent[0])
    for oneContent in everyContent[1:]:
        name, content = oneContent.split('\n', 1)
        settings[name] = content
    with codecs.open(os.path.join(Path["Resources"], settings["Model"]), 'r', 'utf-8') as fin:
        model = fin.read()
        # Debug(model)
        html = model
    for name in settings:
        if name != u"Model":
            if name == u"Content":
                html = html.replace(u'{{%s}}' % name, markdown_html(settings[name]))
            elif name == u"Code":
                html = html.replace(u'{{%s}}' % name, cpp_html(settings[name]))
            else:
                html = html.replace(u'{{%s}}' % name, settings[name])
    with codecs.open(os.path.join(outputPath, article + '.html'), 'w', 'utf-8') as fout:
        # Debug(html)
        fout.write(html)


if __name__ == '__main__':
    pass
