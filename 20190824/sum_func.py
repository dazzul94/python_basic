'''
1부터 100까지 더하는 함수
'''

def sum_func(n):
        s = 0
        for x in range(1, n+1):
            s = s + x
        return s

print(sum_func(100))
