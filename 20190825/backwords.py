'''
임의의 정수 네 자리를 입력 받아 거꾸로 출력하는 프로그램을 작성하시오.
ex) 입력: 1234
    출력: 4321 
'''



input_num = input("임의의 네자리 정수를 입력해주세요")

'''
# 1번째 방법: 문자열 index
print(input_num[3] + input_num[2] + input_num[1] + input_num[0])
print(input_num[-1] + input_num[-2] + input_num[-3] + input_num[-4])
'''

'''
# 2번째 방법: 문자열 split-------> 다시
a, b, c, d = input_num.split()
'''

input_num = int(input_num)

# 3번쨰 방법: 십진수
a = input_num // 1000
b = (input_num % 1000) // 100
c = ( (input_num % 1000) % 100 ) // 10
d = ( (input_num % 1000) % 100 ) % 10

print(d * 1000 + c * 100 + b * 10 + a)

print(str(d) + str(c) + str(b) + str(a))

