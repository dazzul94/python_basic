#!/usr/bin/env python3

import sys
import glob
import os

my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

max_index = len(my_letters)

output_file = sys.argv[1]

filewriter = open(output_file, 'w') # 쓰기 모드로 열기
for index_value in range(len(my_letters)):
    # 9보다 작을 경우 (맨마지막 j 빼고) 탭으로 구분
    if index_value < (max_index - 1):
        filewriter.write(my_letters[index_value] + '\t')
    # 9보다 작지 않을경우(j일때는 엔터)
    else :
        filewriter.write(my_letters[index_value] + '\n')

filewriter.close()

# cmd> writeTxt.py writeTxt.txt