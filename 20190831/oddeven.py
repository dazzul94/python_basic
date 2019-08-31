'''
조건 36535가 짝수인지 홀수인지
'''

print("임의의 정수를 입력하세요.> ")
num = input()
'''
num = int(num)

# 첫번째 방법
if num % 2 == 0 :
    print("짝수입니다.")
else :
    print("홀수입니다.")
'''
'''
# 두번째 방법
last_num = int(num[-1])
if  last_num == 0 \
    or last_num == 2 \
    or last_num == 4 \
    or last_num == 6 \
    or last_num == 8 :
    print("짝수입니다.")
else :
    print("홀수입니다.")
'''
# 세번째 방법
last_num = num[-1]

if last_num in '02468' :
    print("짝수입니다.")
else :
    print("홀수입니다.")