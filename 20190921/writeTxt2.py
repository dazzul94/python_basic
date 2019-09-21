import sys
import glob
import os

my_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_index = len(my_num)

output_file = sys.argv[1]
filewriter = open(output_file, 'a')

for index_value in range(len(my_num)):
    if index_value < (max_index-1):
        filewriter.write(str(my_num[index_value]) + ', ')
    else:
        filewriter.write(str(my_num[index_value]) + '\n')
filewriter.close()

# python writeTxt2.py writeTxt2.txt