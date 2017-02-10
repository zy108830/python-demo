# -*- coding: utf-8 -*-]
import redis, re


# 七牛日志的格式：
# IP - 命中率
# IP - ResponseTime  [time +0800] "Method URL HTTP/1.1" code size "referer" "UA"
class QiniuLog(object):
    def add_count(self, conn, filename):
        if re.match('(.*)\.mp3$',filename):
            count = conn.incr('qiniu_statics:music_link:' + filename)
            conn.zadd(u'qiniu_statics:music_link', filename, count)

    def read_file(self):
        self.conn = redis.Redis(host='127.0.0.1', port=6379, db=0)
        f = open(
            '/usr/local/var/www/zy108830/python-demo/basic_learn/2.0IO编程/resources/qiniu_log/res.psy-1.com_2017-01-15_part-00000')
        reg = re.compile(
            '^(?P<ip>[^ ]*) - (?P<resp_time>[^ ]*) (?P<time>[^"]*) "(?P<method_url_http>[^"]*)" (?P<code>[^ ]*) (?P<size>[^ ]*) "(?P<refer>[^ ]*)" "(?P<ua>[^"]*)"')
        for line in f.readlines():
            regMatch = reg.match(line)
            # 如果有空行就会报错了
            if (regMatch):
                logDict = regMatch.groupdict()
                filename = logDict['method_url_http'].split(' ')[1]
                self.add_count(self.conn, filename)

qiniu_log=QiniuLog()
qiniu_log.read_file()