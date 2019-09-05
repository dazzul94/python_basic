'''
[1, 3, 5, 4, 2] 를 [5, 4, 3, 2, 1]로 바꾸기
'''

a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()

# a.sort().reverse() -> AttributeError: 'NoneType' object has no attribute 'reverse'
# a.sort()가 None을 리턴한다.
print(a)