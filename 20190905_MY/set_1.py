'''
집합 자료형
중복 X, 순서 X(unordered)
'''
s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

# 교집합, 합집합, 차집합
s3 = set([1, 2, 3, 4])
s4 = set([3, 4, 5, 6])

# 교집합
print(s3 & s4) 
print(s3.intersection(s4))

# 합집합
print(s3 | s4) 
print(s3.union(s4))

# 차집합
print(s3 - s4)
print(s3.difference(s4))