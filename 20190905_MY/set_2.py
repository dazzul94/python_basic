# 값 1개 추가하기
s1 = set([1, 2, 3, 4])
s1.add(5)
print(s1)

# 값 여러개 추가하기
s2 = set([1, 2, 3, 4, 5])
s2.update([2, 4, 6, 8, 10])
print(s2)

# 특정 값 제거하기
s3 = set([1, 2, 3, 4, 5])
s3.remove(2)
print(s3)