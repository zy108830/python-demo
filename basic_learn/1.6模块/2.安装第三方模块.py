# -*- coding: utf-8 -*-
# python的第三方模块是根据包管理工具pip来完成的
# 如果python 2.x与python 3.x同时存在,那么就只有pip3,而没有pip了

import sys

#输出我们在引用一个模块时,python的搜索路径
print(sys.path)

##添加搜索路径的方法有两种
##第一种:由于sys.path的数值为list,因此可以通过sys.append()方法添加搜索路径

##第二种:在shell环境中添加PATHONPATH环境变量




