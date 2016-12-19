# 将文件内容转换为map格式
# 例如将
# 1
# 2
# 3
# 转换为
# 1 a
# 2 b
# 3 c

f = open('/Users/xinchao/qiniu_migrate/migrate_headportrait.list2.txt')

fileList = []

for line in f.readlines():
    fileList.append(str.strip(line) + "\t" + "headportrait-bucket/"+line)

with open('/Users/xinchao/qiniu_migrate/migrate_headportrait.list3.txt', 'w') as f:
    for fileName in fileList:
        f.write(fileName)
