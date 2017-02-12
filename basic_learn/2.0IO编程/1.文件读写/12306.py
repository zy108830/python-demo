import os, mysql.connector
from datetime import datetime

# 连接数据库
conn = mysql.connector.connect(user='forge', password='forge', database='train12306')
cursor = conn.cursor()

f = open(os.getcwd() + '/../resources/12306.txt')

for line in f.readlines():
    line = line.strip().replace('\ufeff', '').split('----')
    cursor.execute(
        'insert into train_user (user_account,user_password,user_name,user_idcard,user_nickname,user_mobile,'
        'user_email,create_time) values (%s, %s,%s, %s,%s, %s,%s, %s)',
        [line[0], line[1], line[2], line[3], line[4], line[5], line[6], (int)(datetime.timestamp(datetime.now()))])
    conn.commit()
# # 收尾
cursor.close()
conn.close()