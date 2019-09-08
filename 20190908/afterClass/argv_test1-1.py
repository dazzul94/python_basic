'''
테이블 검색 및 결과물을 CSV 파일로 출력하기
'''
#!/usr/bin/env python3 
import csv 
import MySQLdb 
import sys 
 
# Path to and name of a CSV output file 
output_file = sys.argv[1] 
input_number = sys.argv[2]
# print(input_number)
# print(type(input_number))

 
# Connect to a MySQL database 
con = MySQLdb.connect(host='localhost', port=3309, db='my_suppliers', user='user1', passwd='user1') 
c = con.cursor() 
 
# Create a file writer object and write the header row 
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',') 
header = ['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date'] 
filewriter.writerow(header) 
 
'''
sqlite3 는 ? 쓸수있는데
mysql은 %방식으로 넣어줘야 인식한다.
'''

# Query the Suppliers table and write the output to a CSV file 
c.execute("""SELECT * 
             FROM Suppliers 
             WHERE Cost > %d;""" % int(input_number)) 
rows = c.fetchall() 
for row in rows:  
    filewriter.writerow(row) 

# cmd> python argv_test1-1.py argv_test1-1_csv.csv 700