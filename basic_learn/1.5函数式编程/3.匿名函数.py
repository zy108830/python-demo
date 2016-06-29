#匿名函数的定义,匿名函数不用return,:后面接着的即是return的值
lambda x:x*x

#匿名函数的自执行
print((lambda x:x*x)(16))