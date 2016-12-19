# 注意用到的库和 python 2 有明显不同
from urllib import request
from urllib.parse import quote
from  urllib import error
import urllib
import os

# url = 'http://o96bzfql0.bkt.clouddn.com/Fg1HmYJHYN1azp1q3ORMfAVKTZum'
# with request.urlopen(url) as file:
#     with open("/Users/xinchao/Desktop/"+"aaa", 'wb') as target:
#         target.write(file.read())

f = open('/usr/local/var/qiniu_backup/siguoya/siguoya_xinchao.list2.txt')
for line in f.readlines():
    #如果不加strip，会导致保存下来的文件都带着一个问号，例如aaa.png?
    absPath = ("/usr/local/var/qiniu_backup/siguoya/xinchao/" + line).strip()
    if os.path.isfile(absPath) != True:
        url = "http://7xrc0x.com1.z0.glb.clouddn.com/" + urllib.parse.quote(line.strip())
        try:
            print(url)
            with request.urlopen(url) as file:
                fileDir = os.path.split(absPath)[0]
                if os.path.exists(fileDir) != True:
                    # os.mkdir(fileDir) 不支持递归创建
                    os.makedirs(fileDir)
                with open(absPath, 'wb') as target:
                    target.write(file.read())
        except urllib.error.HTTPError:
            print('errorUrl:' + url)