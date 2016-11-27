import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
# 普通的函数调用只会返回一次,但fork函数比较特殊,它会返回两次
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
# 父进程会返回子进程的ID,子进程会返回0
# 通过os.getpid()函数可以获取当前进程的ID,通过os.getppid()可以
pid = os.fork()
print('返回值为: ', pid)
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
