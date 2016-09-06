import os
import sys


inList = False


def convert_one(line):
    result = ''
    which = ''

    # decide the type of this line
    if line.startswith('#### '):
        which = 'title4'
    elif line.startswith('### '):
        which = 'title3'
    elif line.startswith('## '):
        which = 'title2'
    elif line.startswith('# '):
        which = 'title1'
    elif line.startswith('- '):
        which = 'list'

    # do something
    if inList and which != 'list':
        inList = False
        result += '</ul>\n'

    # convert the content of this line
    if which == 'title4':
        result = '<h4>%s</h4>\n' % line[5:]
    if which == 'title3':
        result = '<h3>%s</h3>\n' % line[4:]
    if which == 'title2':
        result = '<h2>%s</h2>\n' % line[3:]
    if which == 'title1':
        result = '<h1>%s</h1>\n' % line[2:]
    if which == 'list':
        if not inList:
            inList = True
            result = '<ul>\n'
        result += '<li>%s</li>\n' % line[2:]

    # return
    return result


def convert((mdFile, htmlFile)):
    with open(mdFile, 'r') as fin:
        with open(htmlFile, 'w') as fout:
            for line in mdFile.readlines():
                fout.write('%s\n' % convert_one(line[:-1]))


if __name__ == '__main__':
    convert(sys.argv[1:])
