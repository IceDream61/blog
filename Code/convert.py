# -*- coding: utf-8 -*-
"""将我自定义的write格式转换到html格式。
"""


import os
import sys
import time
import markdown


Path = {"Root": "..",
        "Resources": "../Resources",
        "Localsite": "../Localsite",
        "Website": "../Website"
        }


def convert_markdown(content):
    """把一段markdown转换成html
    """
    with open('tmp.md', 'w') as fout:
        fout.write(content)
    os.system('python -m markdown -x markdown.extensions.tables tmp.md > tmp.html')
    with open('tmp.html', 'r') as fin:
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
    if not os.path.exists(os.path.join(Path["Localsite"], article + '.settings')):
        print "Article %s hasn't settings at %s, so give up to convert it." % (article, os.path.join(Path["Localsite"], os.path.join(article, '.settings')))
        return
    print 'convert article: %s' % article
    path, name = os.path.split(article) # 形如："", "index" or "Algorithm", "qsort"
    with open(os.path.join(Path["Localsite"], article + '.settings'), 'r') as fin:
        settings = eval(fin.read())
    with open(os.path.join(Path["Localsite"], article + '.article'), 'r') as fin:
        content = fin.read()
    with open(os.path.join(Path["Resources"], settings["Model"]), 'r') as fin:
        model = fin.read()
    html = model.replace('{{Title}}', settings["Title"]).replace('{{Content}}', convert_markdown(content))
    with open(os.path.join(outputPath, article + '.html'), 'w') as fout:
        fout.write(html)


if __name__ == '__main__':
    pass
