'''
자료형의 모임을 표현하는 List 자료형
리스트명 = [요소1, 요소2, 요소3, ...]
'''

a = [1, 2, 3]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[0] + a[2])
print(a[-1])

b = [1, 2, 3, ['a', 'b', 'c']]
print(b[0])
print(b[-1])

# 리스트에 포함된 리스트의 요소 뽑아내기
print(b[-1][2])

# 리스트 슬라이싱
print(a[0:2])

# 리스트 연산하기
# 리스트 더하기(+)
c = [1, 2, 3]
d = [4, 5, 6]

e = c + d 
print(e)

# 리스트 곱하기(*) : 반복
f = c * 3

print(f)
# 리스트 길이구하기
print(len(f))