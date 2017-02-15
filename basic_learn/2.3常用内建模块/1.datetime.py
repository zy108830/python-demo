# 注意到datetime是模块，datetime模块还包含一个datetime类
# 通过from datetime import datetime导入的才是datetime这个类。
# 如果仅导入import datetime，则必须引用全名datetime.datetime。

from datetime import datetime

# 获取当前时间
now = datetime.now()
print(now)

# 获取时间类型
print(type(now))

# 用指定日期时间创建datetime
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# 将datetime转换为时间戳
print(dt.timestamp())

# 将timestamp转换为datetime
print(datetime.fromtimestamp(1429417200.0))

# 字符串转换为datetime
print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))

# datetime转换为字符串
print(datetime.now().strftime('%a, %b %d %H:%M'))