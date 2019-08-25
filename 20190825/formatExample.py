'''
사용자에게 두 개의 숫자를 각각 입력 받은 후
사칙 연산을 하는 프로그램을 작성하시오.

- error
TypeError: can't multiply sequence by non-int of type 'str'
=> 입력받은 문자열을 int로 바꿔줘야한다.

- 프로그램의 문제점 
a가 b보다 크다라는 전제가 있어야 한다.(두수의 차를 구할때는 큰것에서 작은 것을 뺀다)

'''

print("첫번째 숫자를 입력해주세요")
a = input()

print("두번째 숫자를 입력해주세요")
b = input()

# 형변환
a = int(a)
b = int(b)

# 교환법칙 추가
if a < b: 
    a, b = b, a 

print("두 수의 합은 {0} 입니다".format(a + b))
print("두 수의 곱은 {0} 입니다".format(a * b))
print("두 수의 차는 {0} 입니다".format(a - b))
print("두 수의 나누기는 {0} 입니다".format(a / b))


# 한줄로 표현 
# format함수 이용하는 목적: 여러개 변수 표현하기 위해서
print("두 수의 합, 곱, 차, 나누기는 각각 {0}, {1}, {2}, {3} 입니다".format( (a + b), (a * b), (a - b), (a / b) ))