# #!/usr/bin/env python3      
import sys
import glob
# glob 모듈은 지정된 위치에서 패턴과 일치하는 모든 경로명 탐색
import os
# os 모듈은 하나 이상의 경로를 구성하는 요소들을 합친다.

input_path = sys.argv[1]

# 해당 경로(input_path)에 있는 모든 txt파일을 찾아서 연다.
for input_file in glob.glob(os.path.join(input_path, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))

# python openTxt3.py C:\Users\dazzul\Documents\GitHub\python_basic\20190921\lyrics

# 출력된 걸 하나의 txt파일에 저장하는것은 숙제