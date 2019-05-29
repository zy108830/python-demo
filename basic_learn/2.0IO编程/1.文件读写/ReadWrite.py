# 获取上百G的文件的行数
line_count = 0
with open('/path/to/file', 'r') as f:
    for line in f:
        line_count += 1
        if line_count % 1000 == 0:
            print(line_count)
    print(line_count)
