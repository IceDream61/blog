# -*- coding: utf-8 -*-
"""所有模型。
"""


import os
import sys
import time


class Article(object):
    """一篇文章。

    属性：
        Title: 文章标题。
    """

    def __init__(self, title='无题'):
        """初始化函数。

        输入：
            title: 文章标题，默认值为“无题”。
        """
        self.Title = title


class Algorithm(Article):
    """一篇算法文章。

    暂时只支持由C++代码目录生成。

    属性：
        Path: 代码目录。
        CodeName: 代码名称，约定与文件夹名相同。
        TestCount: 测试数据组数，约定由0开始编号，默认值为1组。
    """

    def __init__(self, path, testCount = 1):
        """初始化函数。

        输入：
            path: 算法目录，暂只支持绝对目录。
        """
        self.Path = path
        self.CodeName = os.path.split(path)[1]
        self.TestCount = testCount
