from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_addr = input('请输入发送人邮箱：')
password = input('请输入邮箱第三方登录授权码：')
# 输入SMTP服务器地址:
smtp_server = input('请输入发送人邮箱所在的SMTP服务器地址：')

# 输入收件人地址:
to_addr = input('请输入收件人邮箱：')

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
msg = MIMEText(input('请输入邮件内容：'), 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header(input('请输入邮件标题：'), 'utf-8').encode()


server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
