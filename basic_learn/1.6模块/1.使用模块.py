#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'A test module'

__AUTHOR__ = 'zqq'

import sys

# 如果直接运行此模块,则此模块的__name__的值为__main__
# 如果此模块被导入到其他模块中运行,则此模块的__name__的值为模块文件名,即'1.使用模块'
# 通过__name__值,可以判断出此模块是被直接调用还是间接调用
print(__name__)

# 用于输出命令行中的传参
# 默认情况下,只会输出[这个文件的路径]
# 如果是python3 this.py zqq yfx,就会输出[这个文件的路径,'zqq','yfx']
print(sys.argv)


#模块的public变量及方法的命名方式是abc,private变量及方法的命名方式就是_abc


