import json, mysql.connector
from datetime import datetime

# 读取内容
f = open('./article.json', 'r')
items = json.loads(f.read())

# 连接数据库
conn = mysql.connector.connect(user='root', password='', database='siguoya')
cursor = conn.cursor()

# 写入数据库
for item in items:
    dt = datetime.strptime(str.replace(item['creat_time'], '发表于', ''), '%Y-%m-%d %H:%M:%S')
    item['create_time'] = int(dt.timestamp())
    cursor.execute(
        'insert into yxl_article (article_title,article_cover,article_link,article_author,article_view,article_favour,article_label,article_collect,article_create_time,article_content) values (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)',
        [item['title'], item['cover'], item['link'], str.strip(item['author']), int(item['view']), int(item['favour']),
         json.dumps(item['label']), int(item['collect']), item['create_time'], item['content']])
    conn.commit()
# 收尾
cursor.close()
conn.close()
