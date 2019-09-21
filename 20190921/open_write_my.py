# #!/usr/bin/env python3      

# 출력된 걸 하나의 txt파일에 저장하는 숙제

import sys
import glob
import os

# 첫번째 아규먼트(lyrics 폴더)
input_path = sys.argv[1]

lyrics = []

# 해당 경로(input_path)에 있는 모든 txt파일을 찾아서 연다.
for input_file in glob.glob(os.path.join(input_path, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
           # print("{}".format(row.strip()))
           lyrics.append(row.strip())

max_index = len(lyrics)

# 두번째 아규먼트(write 파일)
output_file = sys.argv[2]
'''
filewriter = open(output_file, 'w') # 쓰기 모드로 열기
for index_value in range(len(lyrics)):
    if index_value < (max_index):
        filewriter.write(lyrics[index_value] + '\n')
filewriter.close()
'''

# with문
with open(output_file, 'w') as file:
    for line in lyrics:
        file.write(line + '\n')

# python open_write_my.py C:\Users\dazzul\Documents\GitHub\python_basic\20190921\lyrics open_write_my.txt
