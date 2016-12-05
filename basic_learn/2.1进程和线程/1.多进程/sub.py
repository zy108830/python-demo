import subprocess

print('$ nslookup www.python.org')
# subprocess模块可以让我们非常方便地启动一个子进程, 以下语句和在命令行中nslookup www.python.org效果是一样的
r = subprocess.call(['nslookup', 'www.python.org'])
r2 = subprocess.call(['ls', '-al', '/'])
print('Exit code:', r)
print('Exit code:', r2)

# 如果我们还需要输入额外的信息,可以使用communicate()
# 下面的代码相当于在命令行执行命令nslookup，然后手动输入：
# set q=mx
# python.org
# exit

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
