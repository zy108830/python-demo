# -*- coding: utf-8 -*-
import os,mysql.connector

conn=mysql.connector.connect(user='root', password='', database='qiniu')
cursor = conn.cursor(buffered=True)

f=open(os.getcwd()+'/../resources/qiniu_file/20170214.txt')
for line in  f.readlines():
    file_info=line.split('	')
    cursor.execute('INSERT INTO qiniu_file(file_url,file_time,file_type) VALUES (%s,%s,%s)',
                   ['https://res.psy-1.com/'+file_info[0].strip(),(int)(file_info[3][0:10]),file_info[4]])
    conn.commit()
