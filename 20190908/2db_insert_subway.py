#!/usr/bin/env python3
import csv
import sqlite3
import sys

input_file = sys.argv[1] # 명령어에서 파일지정(subway)

con = sqlite3.connect('Subway.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Subway 
                                (ID INT,
                                Station VARCHAR(20),
                                Weekday INT,
                                Saturday INT,
                                Sunday INT);"""
c.execute(create_table)
con.commit()

file_reader = csv.reader(open(input_file, 'r', encoding='UTF8'), delimiter = ',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
            data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO Subway VALUES(?, ?, ?, ?, ?);", data)
con.commit()

output = c.execute("SELECT * FROM Subway")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)

# 2db_insert_subway
# cmd> python 2db_insert_subway.py suppliers_data.csv