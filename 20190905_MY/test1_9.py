'''
오류가 발생하는 경우, 그 이유 고르기
'''
a = dict()
print(a)

# 1. a['name'] = 'python'
# 2. a[('a,')] = 'python'
# 3. a[[1]] = 'python'
# 4. a[250] = 'python'

# 3번, 이유: 딕셔너리의 키값에는 리스트가 들어올 수 없다. 키값이 변하면 안되기 때문이다.

a['name'] = 'python'
a[('a,')] = 'python'
a[250] = 'python'
# a[[1]] = 'python'
print(a)