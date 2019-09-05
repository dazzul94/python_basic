# 리스트에 a번째 위치에 b를 삽입(inser(a,b))
a = [1, 2, 3, 4]
a.insert(1, 'a')
print(a)

# 리스트에 첫번째 나오는 x를 삭제(remove(x))
b = [1, 2, 3, 4, 3]
b.remove(3)
print(b)

# 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제(pop())
c = [1, 2, 3, 4]
print(c.pop())
print(c)

# 리스트의 x번째 요소를 돌려주고 그 요소를 삭제(pop(x))
d = [1, 2, 3, 4]
print(d.pop(2))
print(d)

# 리스트에 포함된 x 개수 세기(count)
e = [1, 2, 3, 4, 1, 1, 1]
print(e.count(1))

# 리스트 확장(extend)
f = [1, 2, 3]
f.extend([3, 4, 5])
print(f)
