#!/usr/bin/env python3
import sqlite3

# DB를 생성하고 4개의 속성을 가진 sales 테이블을 생성한다.
con = sqlite3.connect('C:/Users/dazzul/Documents/GitHub/python_basic/20190908/new_db.sql') # 하드에 저장
query = """CREATE TABLE SALES (
customer VARCHAR(20),
product VARCHAR(40),
amount FLOAT,
date DATE);
"""

con.execute(query)
con.commit()

# SALES 테이블에 데이터 삽입
data = [('Richard Lucas', 'Notepad', 2.50, '2019-5-1'),
        ('Jenny Kim', 'Binder', 4.15, '2019-6-6'),
        ('Svetlana Crow', 'Printer', 155.75, '2019-7-7'),
        ('Stepheny Randoph', 'Computer', 679.40, '2019-8-8')]
statement = "INSERT INTO SALES VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()

# SALES 테이블에 질의하기
cursor = con.execute("SELECT * FROM SALES")
rows = cursor.fetchall()

# 출력된 데이터의 수를 센다.
row_counter = 0
for row in rows :
    print(row)
    row_counter += 1
print()
print("Number of rows: {}".format(row_counter))

# 저장파일명: 1db_count_rows.py
# cmd> python 1db_count_rows.py


