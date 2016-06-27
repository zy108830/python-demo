# -*- coding: utf-8 -*-
# 切片操作,获取数组中的指定区域
nums=[0,1,2,3,4,5,6,7,8,9]

#复制
print(nums[:])

#取前两个
print(nums[0:2])
#取后三个
print(nums[-3:])

#每两个取一个
print(nums[::2])
#前五个,每两个取一个
print(nums[:5:2])