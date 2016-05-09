# namedtuple 用于创建可以通过自定义的属性来引用集合元素的集合
from collections import namedtuple
from collections import deque
from collections import defaultdict

Users = namedtuple('User', ['name', 'age'])
person = Users('zqq', 24)
print(person.name, person.age)

# 判断是否为集合的实例
print(isinstance(person, Users))
print(isinstance(person, tuple))

# 高效地对集合执行插入和删除操作:append,pop,apendleft,popleft
data = deque(['a', 'b', 'c'])
data.append('x')
data.appendleft('y')
print(data)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict

# Counter
