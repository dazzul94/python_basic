# 셔뱅 -> 유닉스, 리눅스 기반에서 사용한다. 윈도우에서는 동작하지 않는다.
# #!/usr/bin/env python3      

'''
- 파이썬 함수는 크게 3가지로 구분
1) 내장함수 -> 파이썬에서 기본으로 제공하는 함수 ex) print()
2) 외장함수 -> 파이썬에 파일로 저장되어있지만 기본제공안됨. 
               호출하고싶으면 import명령으로 모듈을 호출하여 사용
3) 사용자정의함수 -> 사용자가 필요에 따라 생성하여 사용한다.
   ex) def 함수명:
'''

import sys
# sys모듈을 사용하면 리스트 형식의 argv 변수를 사용할 수 있다.
# 이 변수를 명령줄 인수들로 구성된 리스트를 파이썬 스크립트로 가져온다.
# 다른 리스트와 마찬가지로 argv는 인덱스를 갖는다.

print("Output: /lyrics/2002.txt")
print()

# 스크립트 파일 실행시 이름을 지정한다.
# sys.argv[0], sys.argv[1], sys.argv[2]
# sys.argv[0]는 스크립트 파일 자체를 의미하기 때문에 스크립트 내에 사용금지
input_file = sys.argv[1]
filereader = open(input_file, 'r') # 읽기 전용으로 연다.

for row in filereader :
    print(row.strip()) # 스트링의 양쪽 공백을 모두 지운다.
filereader.close()

# python openTxt.py lyrics/2002.txt
