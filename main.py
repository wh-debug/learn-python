# -*- coding: UTF-8 -*-
"""
    学习argparse模块总结:
        通过argparse模块，可以轻松编写用户友好的命令行界面。 它解析sys.argv中定义的参数。
        argparse模块还会自动生成帮助和使用消息，并在用户为程序提供无效参数时发出错误。
        argparse是标准模块； 我们不需要安装它。
        使用ArgumentParser创建一个解析器，并使用add_argument()添加一个新参数。 参数可以是可选的，必需的或定位的。
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help='shows output')
args = parser.parse_args()

if args.output:
    print("This is some output")
