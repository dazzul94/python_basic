'''
테이블에 새 레코드 입력하기
'''
#!/usr/bin/env python3 
import csv 
import MySQLdb 
import sys 
from datetime import datetime, date

# Path to and name of a CSV input file 
input_file = sys.argv[1] 
 
# Connect to a MySQL database 
con = MySQLdb.connect(host='localhost', port=3309, db='my_suppliers', user='user1', passwd='user1') 
# 원격 접속하려면 host에 ip주소 입력
# con = MySQLdb.connect(host='192.168.0.156', port=13306, db='my_suppliers', user='root', passwd='1111') 
c = con.cursor() 
 
# Read the CSV file 
# Insert the data into the Suppliers table 
file_reader = csv.reader(open(input_file, 'r'), delimiter=',') 
header = next(file_reader) 
for row in file_reader:  
    data = []  
    for column_index in range(len(header)):   
        if column_index < 4:    
            data.append(str(row[column_index]).lstrip('$')\
            .replace(',', '').strip())   
        else:    
            a_date = datetime.date(datetime.strptime(\
            str(row[column_index]), '%m/%d/%y')) 
            # %Y: year is 2016; %y: year is 15    
            a_date = a_date.strftime('%Y-%m-%d')    
            data.append(a_date)  
    print(data)  
    c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data) 
con.commit() 
 
# Query the Suppliers table 
c.execute("SELECT * FROM Suppliers") 
rows = c.fetchall() 
for row in rows:  
    row_list_output = []  
    for column_index in range(len(row)):   
        row_list_output.append(str(row[column_index]))  
        print(row_list_output) 
 
 # cmd> python 4db_mysql_load_from_csv.py suppliers_data.csv
