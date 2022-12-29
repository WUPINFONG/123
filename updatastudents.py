# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:05:24 2022

@author: perry
"""

import db
print('修改學生資料')
sql='select su_no from students'
cursor = db.conn.cursor()
cursor.execute(sql)
db.conn.commit()

result=cursor.fetchall()#抓取全部的資料
print(result)
print('學號')
for row in result:
    print(row[0])

no=input('請輸入學號:')
tel=input('請輸入預修改的電話:')
mobile=input('請輸入預修改的行動電話:')
sql="update students set tel='{}',mobile='{}' where su_no='{}'".format(tel,mobile,no)
cursor.execute(sql)
db.conn.commit()

db.conn.close()